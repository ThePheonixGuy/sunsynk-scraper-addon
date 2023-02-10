# Changelog

## 0.2.11

- Added default values for non-home-assistant installations
- Fixed a crash introduced in 0.2.10 affecting home-assistant installations

## 0.2.10

- Allow insecure mqtt for non-home-assistant installations

## 0.2.9 

- Debug log until start initi is complete

## 0.2.8

- Fixes loss of PV data

## 0.2.6

- Fix divide by zero error when API gives faulty data

## 0.2.5

- Add debug logging for failing to connect to MQTT
- Fix logger formatting error to allow failures to propogate properly

## 0.2.0

- Full refactor of structures for MQTT publishing into models
- Full refactor of API Integration
- Better handling of sensor entities going forward
- Add icon support for sensor entities

## 0.1.1

- Adds binary sensor support to publish charging status.
- Use asyncio to prevent MQTT connection lockups and failures
- Better protection against API failures

## 0.1.0

First running version.
