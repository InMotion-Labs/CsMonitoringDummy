import logging
import math
import random
import time

import requests

import settings

settings.init()

if settings.conf['logs'] is not None:
    logging.basicConfig(filename=settings.conf['logs'], format='%(asctime)s - %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)
else:
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)

url = settings.conf["url_grafana"]

system = settings.conf["system"]
category = settings.conf["category"]
subcategory = settings.conf["sub-category"]

headGroup = settings.conf['group_head']
mainBoardGroup = settings.conf['group_MainBoard']
applicationGroup = settings.conf['group_Application']

groupHeadSubGroup = settings.conf['sub-group_head']
groupMainBoardSubGroup = settings.conf['sub-group_MainBoard']
groupApplicationSubGroup = settings.conf['sub-group_Application']

session = requests.Session()
# session.headers.update({'x-auth-token': (settings.conf["x-auth-token"])})

timeToInsert = (int(time.time()) - 12 * 60 * 60) * 1000  # minus 12 hours so it will looks nice


def build_value_body(min_value, max_value, generator_seed, body_group, body_subgroup, value_name):
    middle = (min_value + max_value) / 2
    diff = max_value - middle
    base = math.sin(
        ((time.time() + generator_seed) * (0.8 + (generator_seed % 100 / 1000) * 4)) * 0.01745329252) * diff + middle
    noise = (random.random() - 0.5) * generator_seed % (diff / 10)
    value = base + noise
    return (f'datadouble;'
            f'{system};{category};{subcategory};'
            f'{body_group};{body_subgroup};'
            f'{value_name};'
            f'{value};'
            f'{timeToInsert}')


def build_annotation_body(body_group, body_subgroup, annotation_body, tag):
    return (f'annotation;'
            f'{system};{category};{subcategory};'
            f'{body_group};{body_subgroup};'
            f'placeholder;'
            f'{annotation_body};'
            f'{tag};'
            f'{timeToInsert}')


logging.info("Program start")
logging.info("System: " + system)
logging.info("Category: " + category)
logging.info("Subcategory: " + subcategory)

if settings.conf["clear-previous"]:
    response = session.delete(
        f'{url}api/v_0/data/double/delete/{system}?from={timeToInsert - 60 * 60}&to={timeToInsert + 12 * 60 * 60}')
    response = session.delete(
        f'{url}api/v_0/data/annotation/delete/{system}?from={timeToInsert - 60 * 60}&to={timeToInsert + 12 * 60 * 60}')

valueBodies = []
annotationBodies = []

to = 12 * 60
for i in range(0, to):

    randint = random.randint(0, 1000)

    if randint > 985:
        text = (f'Device Paired: <br>'
                f'Min Internal Temperature: {random.randint(-20, 50)} <br> '
                f'Max Internal Temperature: {random.randint(-20, 50)} <br> '
                f'Min External Temperature: {random.randint(-20, 50)} <br> '
                f'Max External Temperature: {random.randint(-20, 50)} <br> '
                f'Running Time: {random.randint(0, 4294967295)} <br> '
                f'App version: 3.0.65 <br> '
                f'Firmware revision: x.y.z <br> '
                f'Hardware revision: 3.36 <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_Application"],
                                  settings.conf["sub-group_Application"],
                                  text,
                                  "on_pair"))

    if 940 < randint < 960:
        text = (f'Before photo: <br>'
                f'PitchAnglee: {random.randint(-180, 180)} <br> '
                f'RollAngle: {random.randint(-180, 180)} <br> '
                f'YawAngle: {random.randint(0, 360)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_Application"],
                                  settings.conf["sub-group_Application"],
                                  text,
                                  "before_photo"))

    if 890 < randint < 900:
        text = (f'Charging Flag changed: <br> '
                f'Flag value: {random.random() > 0.5} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "power"))

    if 795 < randint < 800:
        text = (f'IMU DetectFlag: <br> '
                f'Flag value: {random.random() > 0.5} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    if 695 < randint < 700:
        text = (f'Status: <br> '
                f'Flag value: {random.randint(0, 255)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    if 595 < randint < 600:
        text = (f'Error: <br> '
                f'Flag value: {random.randint(0, 255)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    if 495 < randint < 500:
        text = (f'OpMode: <br> '
                f'Flag value: {random.randint(0, 255)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    if 395 < randint < 400:
        text = (f'PowerMode: <br> '
                f'Flag value: {random.randint(0, 255)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    if 295 < randint < 300:
        text = (f'SelfTest: <br> '
                f'Flag value: {random.randint(0, 255)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    if 195 < randint < 200:
        text = (f'StabilizationStatus: <br> '
                f'Flag value: {random.randint(0, 255)} <br> '
                f'')
        annotationBodies.append(
            build_annotation_body(settings.conf["group_head"],
                                  settings.conf["sub-group_head"],
                                  text,
                                  "imu"))

    valueBodies.append(
        build_value_body(-180, 180, 237,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "PitchAngle"))
    valueBodies.append(
        build_value_body(-180, 180, 21,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "RollAngle"))
    valueBodies.append(
        build_value_body(0, 360, 42425,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "YawAngle"))
    valueBodies.append(
        build_value_body(-20, 50, 3578,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "InternalTemp"))
    valueBodies.append(
        build_value_body(-20, 50, 18520,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "ExternalTemp"))
    valueBodies.append(
        build_value_body(0, 100, 7865,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "BatteryCharge"))
    valueBodies.append(
        build_value_body(0, 100, 75745,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "BatteryHealth"))
    valueBodies.append(
        build_value_body(0, 65535, 124,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "BatteryTimeLeft"))
    valueBodies.append(
        build_value_body(0, 50000, 7410,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "BatteryCycles"))
    valueBodies.append(
        build_value_body(0, 5000, 852,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "InputChargingCurrent"))
    valueBodies.append(
        build_value_body(0, 5000, 2586,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "BatteryChargingCurrent"))
    valueBodies.append(
        build_value_body(0, 5000, 6523,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "BatteryVoltage"))
    valueBodies.append(
        build_value_body(-5000, 5000, 96321,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],

                         "BatteryCurrent"))
    valueBodies.append(
        build_value_body(0, 5000, 741852,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "5VBusCurrent"))
    valueBodies.append(
        build_value_body(0, 6000, 100,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "5VBusVoltage"))
    valueBodies.append(
        build_value_body(0, 10000, 963,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "9VBusVoltage"))
    valueBodies.append(
        build_value_body(0, 2000, 2586,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "9VBusCurrent"))
    valueBodies.append(
        build_value_body(0, 15000, 6464,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "ChargingBusVoltage"))
    valueBodies.append(
        build_value_body(0, 5000, 7785364,
                         settings.conf["group_head"],
                         settings.conf["sub-group_head"],
                         "ChargingBusCurrent"))

    timeToInsert += (10 * 6) * 1000

    if len(valueBodies) > 500 or i - 1 == to:
        timestamp = time.time()
        try:
            logging.info("")
            logging.info("Sending Request: Value")
            response = session.post(f'{settings.conf["url_grafana"]}',
                                    headers={'content-type': 'text/plain'}, timeout=settings.conf["timeout"],
                                    data="\n".join(valueBodies))
            logging.info("Response: %s" % response)
        except requests.exceptions.RequestException as e:
            logging.error("Body post failure")
            logging.error(e)

        logging.info(f'Sent in {time.time() - timestamp}[s] len:{len(valueBodies)}')
        valueBodies = []

    if len(annotationBodies) > 0:
        timestamp = time.time()
        # for body in annotationBodies:
        try:
            logging.info("")
            logging.info("Sending Request: Annotation")
            response = session.post(f'{settings.conf["url_grafana"]}',
                                    headers={'content-type': 'text/plain'}, timeout=settings.conf["timeout"],
                                    data="\n".join(annotationBodies))
            logging.info("Response: %s" % response)
        except requests.exceptions.RequestException as e:
            logging.error("Body post failure")
            logging.error(e)
        logging.info(f'Sent in {time.time() - timestamp}[s] len:{len(annotationBodies)}')
        annotationBodies = []
