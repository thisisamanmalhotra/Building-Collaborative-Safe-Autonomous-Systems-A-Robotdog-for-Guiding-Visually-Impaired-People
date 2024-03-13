# Building Collaborative Safe Autonomous Systems: A Robotdog for Guiding Visually Impaired People

## Abstract

This paper presents a summary of a use case involving a robotdog dedicated to guiding visually impaired individuals in complex environments, such as smart intersections. In these scenarios, the robotdog autonomously determines whether it is safe to cross the intersection to guide the human further. We propose a system architecture that facilitates data sharing and collaboration between the robotdog and other autonomous systems operating in the same environment. Our approach involves the separation of the collaborative decision layer to enable collective decision-making processes where data about the environment, relevant to the robotdog's decision, are shared along with evidence for trustworthiness.

## Authors

- Aman Malhotra, Chair of Embedded Systems, TU Dortmund University, Dortmund, Germany, Email: aman.malhotra@tu-dortmund.de
- Selma Saidi, Chair of Embedded Systems, TU Dortmund University, Dortmund, Germany, Email: selma.saidi@tu-dortmund.de

## Introduction

Autonomous systems are increasingly vital across various domains, including mobility and human-assistive robotics. In the context of human-assistive robotics, particularly for social care, there is significant potential for aiding individuals with disabilities. However, ensuring the safe and correct behavior of such systems in dynamic and complex environments poses significant challenges. This paper focuses on the use case of robotdogs guiding blind and visually impaired individuals. Similar to traditional guide dogs, ensuring safety is paramount in the design of these systems, including aspects such as traffic awareness, identifying obstacles or hazards, and guiding the handler safely in public environments. The paper addresses the development of decision-making processes for safety-critical autonomous systems, specifically in scenarios like smart intersections, where the robotdog must autonomously decide on safe crossing without colliding with other autonomous systems or pedestrians. We propose a collaborative framework that enables autonomous systems to leverage collective decision-making processes to enhance reliability and safety.

## Problem Statement

The main challenge addressed in this paper is the development of decision-making processes for ensuring the safety of autonomous systems, particularly in scenarios involving human-assistive robotics, such as guiding visually impaired individuals through complex environments like smart intersections. The key problems include:

- Autonomous determination of safe crossing in dynamic environments.
- Collaboration between autonomous systems to ensure collective decision making.
- Reduction of errors and improvement of decision outcomes through data sharing and aggregation.

## Proposed Solution

To address the aforementioned challenges, we propose a collaborative framework that facilitates collective decision-making processes among autonomous systems. The proposed solution involves:

1. **System Architecture**: We propose a system architecture that supports collaborative approaches for autonomy and decision making. A critical aspect of the design is the separation between the decision layer and other sensing and actuating functionalities.

2. **Data Sharing and Collaboration**: The system enables autonomous systems to share information and aggregate data relevant to decision-making processes. By leveraging collective intelligence, the aim is to reduce errors and improve decision outcomes, particularly in safety-critical scenarios like guiding visually impaired individuals in complex environments.

## Conclusion

This paper presents a summary of a use case involving a robotdog dedicated to guiding visually impaired individuals in complex environments. By proposing a collaborative framework and system architecture, we aim to address the challenges of ensuring safety and reliability in autonomous systems operating in dynamic environments. Through data sharing and collective decision-making processes, we strive to enhance the autonomy and safety of human-assistive robotics, particularly in scenarios such as smart intersections.

## References

[1] Lead Academy. dog. [https://lead-academy.org/blog/how-much-does-it-cost-to-train-a-guide-dog/](https://lead-academy.org/blog/how-much-does-it-cost-to-train-a-guide-dog/).

[2] ROS Wiki. Ros master slave api. [https://wiki.ros.org/](https://wiki.ros.org/).

[3] Selma Saidi. Collective reasoning for safe autonomous systems, 2023.

[4] Selma Saidi, Dirk Ziegenbein, Jyotirmoy V. Deshmukh, and Rolf Ernst. Autonomous systems design: Charting a new discipline. IEEE Design Test, 39(1):8–23, 2022.

[5] Shaoshan Liu and Jean-Luc Gaudiot. Ieee international roadmap for devices and systems (irds) autonomous machine computing white paper 2022. 2022.

---
For further inquiries, please contact the authors.






Sure, here's the README.md file:

```markdown
# TrustAPI Documentation

## Overview

TrustAPI is an API service that facilitates the sharing of sensor data among systems and provides responses regarding the most trustworthy sensor among the inputs provided. This API is designed to handle up to three sensor inputs currently, with a session time set to 10 inputs.

## Authentication

To access the TrustAPI, users need to provide authentication credentials in the HTTP headers. The credentials must be encoded in Base64 format and included in the `Authorization` header.

```python
import base64

# Authentication details
username = 'your_username'
password = 'your_password'

# Encoding credentials
credentials = base64.b64encode(f'{username}:{password}'.encode()).decode()
```

## Usage Example

Below is an example code demonstrating how to use TrustAPI to submit sensor readings and receive responses regarding the most trustworthy sensor:

```python
import requests
import base64
import secrets

url = 'https://trustapi.example.com/'

# Authentication details
username = 'your_username'
password = 'your_password'

# Encoding credentials
credentials = base64.b64encode(f'{username}:{password}'.encode()).decode()

# Defining sensor values
sensor_values = {
    "sensor1": 0.5,
    "sensor2": 0.6,
    "sensor3": 0.7
}

# Generating session nonce
session_nonce = secrets.token_hex(32)

# Setting headers with session nonce
headers = {
    'Authorization': f'Basic {credentials}',
    'TrustAPI-Session-Nonce': session_nonce
}

# Making 15 POST requests
for _ in range(15):
    # Building data payload
    data = {"sensor_readings": sensor_values}

    # Making POST request
    response = requests.post(url, json=data, headers=headers)

    # Printing the response
    print(response.text)
```

## API Endpoints

### POST /sensor_readings

This endpoint is used to submit sensor readings to the TrustAPI. The request should include a JSON object containing sensor readings as key-value pairs. The API will analyze the provided sensor data and determine the most trustworthy sensor among them.

#### Request Body

```json
{
  "sensor_readings": {
    "sensor1": 0.5,
    "sensor2": 0.6,
    "sensor3": 0.7
  }
}
```

#### Response

The response will contain information about the most trustworthy sensor and its corresponding reading.

```json
{
  "most_trustworthy_sensor": "sensor3",
  "reading": 0.7
}
```

## Rate Limiting

The TrustAPI is limited to 10 inputs per session. After reaching the session limit, users need to initiate a new session by including a new session nonce in the headers of subsequent requests.

## Error Handling

In case of errors, the API will return appropriate HTTP status codes along with error messages in the response body.

## Conclusion

TrustAPI provides a simple yet powerful interface for sharing sensor data and determining the most trustworthy sensor among them. With its straightforward authentication mechanism and intuitive endpoints, developers can seamlessly integrate TrustAPI into their systems for enhanced sensor data analysis.
```

You can copy this text and save it as README.md in your project directory.
