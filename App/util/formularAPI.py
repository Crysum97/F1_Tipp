import fastf1
import pandas
import requests
from xml.etree import ElementTree as ET


def get_remaining_events():
    call = pandas.DataFrame(fastf1.get_events_remaining())
    return [{"Event": {"Name": row["EventName"], "Country": row["Country"], "Date": row["EventDate"]},
             row["Session1"]: {"Date": row["Session1Date"]}, row["Session2"]: {"Date": row["Session2Date"]},
             row["Session3"]: {"Date": row["Session3Date"]}, row["Session4"]: {"Date": row["Session4Date"]},
             row["Session5"]: {"Date": row["Session5Date"]}, row["Session5"]: {"Date": row["Session5Date"]}}
            for i, row in call.iterrows()]

def get_upcoming_event():
    return get_remaining_events()[0]


def get_last_result():
    call = requests.get('http://ergast.com/api/f1/current/last/results')
    if call.status_code == 200:
        content = call.text
        tree = ET.fromstring(content)
        ns = {'mrd': 'http://ergast.com/mrd/1.5'}
        results_dict = {}

        for result in tree.findall(".//mrd:Result", ns):
            position = result.attrib['position']
            driver = result.find('mrd:Driver', ns)
            given_name = driver.find('mrd:GivenName', ns).text
            family_name = driver.find('mrd:FamilyName', ns).text
            status = result.find('mrd:Status', ns).text
            full_name = f"{given_name} {family_name}"

            results_dict[full_name] = {"Position": position, "Status": status}
        meta = tree.findall(".//mrd:Race", ns)[0]
        season = meta.attrib['season']
        name = meta.find('mrd:RaceName', ns).text
        results_dict["Event"] = {"Name": name, "Season": season}
        return results_dict
    else:
        return []


def get_current_driverstanding():
    call = requests.get("http://ergast.com/api/f1/current/driverStandings")
    if call.status_code == 200:
        content = call.text
        tree = ET.fromstring(content)
        ns = {'mrd': 'http://ergast.com/mrd/1.5'}
        results_list = []
        for result in tree.findall(".//mrd:DriverStanding", ns):
            position = result.attrib['position']
            points = result.attrib['points']
            driver = result.find('mrd:Driver', ns)
            given_name = driver.find('mrd:GivenName', ns).text
            family_name = driver.find('mrd:FamilyName', ns).text
            full_name = f"{given_name} {family_name}"
            results_list.append({"Name": full_name, "Position": position, "Points": points})
        return results_list
    else:
        return []


def get_last_result_by_name(driver_name):
    result = get_last_result()
    re = [result.get(driver_name), result.get("Event")]
    return re


def get_current_constructorstanding():
    call = requests.get("http://ergast.com/api/f1/current/constructorStandings")
    if call.status_code == 200:
        content = call.text
        tree = ET.fromstring(content)
        ns = {'mrd': 'http://ergast.com/mrd/1.5'}
        results_list = []
        for result in tree.findall(".//mrd:ConstructorStanding", ns):
            position = result.attrib['position']
            points = result.attrib['points']
            constructor = result.find('mrd:Constructor', ns)
            name = constructor.find('mrd:Name', ns).text
            results_list.append({"Name": name, "Position": position, "Points": points})
        return results_list
    else:
        return []

