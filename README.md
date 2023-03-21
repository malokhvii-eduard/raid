<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->

<div align="center">
  <h2 align="center">📢 Raid</h2>
  <p align="center">
    A simple tool to get immediate notifications in Slack once your Ukrainian
    colleagues become unavailable due to an air raid or artillery shelling
    threats.
  </p>

  <p id="shields" align="center" markdown="1">

[![License](https://img.shields.io/badge/license-MIT-3178C6?style=flat)](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][github-pre-commit]
[![Style Guide](https://img.shields.io/badge/code%20style-black-000?style=flat)][github-black]
[![markdownlint](https://img.shields.io/badge/linter-markdownlint-000?style=flat)][github-markdownlint]
[![commitlint](https://img.shields.io/badge/linter-commitlint-F7B93E?style=flat)][github-commitlint]
[![flake8](https://img.shields.io/badge/linter-flake8-3776AB?style=flat)][github-flake8]
[![bandit](https://img.shields.io/badge/linter-bandit-FFC107?style=flat)][github-bandit]
![CI Workflow](https://github.com/malokhvii-eduard/raid/actions/workflows/ci.yml/badge.svg)
[![Release Workflow](https://github.com/malokhvii-eduard/raid/actions/workflows/release.yml/badge.svg)](https://github.com/malokhvii-eduard/raid/)

  </p>
</div>

## 🎉 Features

- 🚀 Easy to use
- 🔖 Mention specific colleagues by area
- 🌍 Multi-language
- 🤝 Free, but you can make a donation to charity funds in Ukraine

## 🌻 Motivation

This tool is specifically designed to provide real-time updates on the safety
status of colleagues in Ukraine during air raids or artillery shelling threats.
It monitors an official Telegram channel that publishes threat notifications and
sends an immediate Slack notification upon detection of a threat. The
notification includes crucial information about the nature and location of the
threat, enabling colleagues to take appropriate measures quickly and efficiently.

In addition, the tool allows for the efficient coordination and communication
of all colleagues located in the affected area during a crisis. It can also
mention specific colleagues by the area in which they are located, enabling them
to coordinate and communicate more efficiently with one another. Organizations
with colleagues working in Ukraine, who may be at risk of exposure to the
Russian-Ukrainian war, can benefit greatly from this project for free. By
proactively managing risks and prioritizing their employees' well-being,
organizations can leverage this tool to safeguard their employees' safety.

## ✨ Getting Started

### 📦 Installation

1. Clone the *Repository*
2. Install this *Package* (`./poetry install`)
3. Get *Telegram API identifier and key*
4. Create a *Slack icoming webhook*

### 👀 Usage

```bash
raid --help # Show help and exit
raid --version # Show version and exit

raid # Notify about threats in all areas
raid --locale en # Send notifications in English

# Mention specific colleagues by area. Prepare a CSV file with two columns:
# a 'member_id' and an area 'hashtag'. You can find area hashtags in a
# Telegram channel @air_alert_ua
raid --members ./members.csv
raid --ignore-without-mentions # Skip notifications without mentions
```

## ❓ FAQs

<!-- FAQ 1 -->
<!-- markdownlint-disable MD013 -->
### 🙋‍♂️ How to get the Telegram API identifier and key?
<!-- markdownlint-enable MD013 -->

👉 To use the Telegram API, you will need to register your application and
obtain API ID and API key. To do this, follow these steps:

1. Go to the [Telegram API website][telegram-api] and log in
using your Telegram account
2. Click on the *"Create a new application"* button and fill in the required
details, including the name and description of your application
3. Once you have registered your app, you will be provided with an API key and
an API identifier. Keep these credentials safe, as you will need them to
integrate the Telegram API into the `raid`

🎉👍 That's it! Now you have Telegram API identifier and key.

<!-- FAQ 2 -->
<!-- markdownlint-disable MD013 -->
### 🙋‍♂️ How to create a Slack icoming webhook?
<!-- markdownlint-enable MD013 -->

👉 To create a new webhook integration in Slack, you will need to be a member
of the workspace and have administrative access. Here's how to create a new
webhook integration:

1. Go to your Slack workspace and click on the gear icon to access the settings
2. Click on *"Add apps"* and search for *"Incoming Webhooks"* in the search bar
3. Click on *"Add to Slack"* and choose the channel you want the webhook to post
messages to
4. Click on *"Authorize"* to authorize the integration

Once you have created the webhook, you will need to configure it by setting the
default username and icon, and customizing any other settings you want. Here's
how to configure the webhook:

1. Click on the *"Webhooks"* section in the integration settings and copy the
webhook URL
2. Choose a default username and icon for your webhook messages
3. Customize any other settings you want, such as message formatting or
notification preferences

🎉👍 That's it! Now you have a webhook integration in Slack.

<!-- FAQ 3 -->
<!-- markdownlint-disable MD013 -->
### 🙋‍♂️ How to find a Slack member ID?
<!-- markdownlint-enable MD013 -->

👉 To find a Slack member ID, you can use one of the following methods:

🔒 Use the Slack API. If you have access to the Slack API:

1. Go to the [Slack API documentation][slack-api-users-list] and find the
`users.list` method
2. Click on the *"Test Method"* button to try out the method. Authenticate with
your Slack account and workspace. Once authenticated, the API will return a
list of users in your workspace along with their user IDs

🔓 Use the Slack web app. If you don't have access to the Slack API:

1. Go to your Slack workspace and open the member's profile page
2. Click on the three dots in the upper-right corner of the profile page and
select *"Copy member ID"* from the dropdown menu. The member ID will be copied
to your clipboard, and you can paste it wherever you need it

🎉👍 That's it! With these methods, you should be able to find a Slack member ID
quickly and easily.

<!-- FAQ 4 -->
<!-- markdownlint-disable MD013 -->
### 🙋‍♂️ Where does the data come from?
<!-- markdownlint-enable MD013 -->

👉 Data is taken from a Telegram channel [@air_alert_ua][telegram-air-alert-ua].

## 🛠️ Tech Stack

<!-- markdownlint-disable MD013 -->
[![EditorConfig](https://img.shields.io/badge/EditorConfig-FEFEFE?logo=editorconfig&logoColor=000&style=flat)][editorconfig]
![Markdown](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=flat)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
[![Typer](https://img.shields.io/badge/Typer-4EAA25?logo=gnubash&logoColor=fff&style=flat)][github-typer]
![Telegram API](https://img.shields.io/badge/Telegram%20API-26A5E4?logo=telegram&logoColor=fff&style=flat)
![Slack SDK](https://img.shields.io/badge/Slack%20SDK-4A154B?logo=slack&logoColor=fff&style=flat)
[![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?logo=precommit&logoColor=fff&style=flat)][github-pre-commit]
[![markdownlint](https://img.shields.io/badge/markdownlint-000?logo=markdown&logoColor=fff&style=flat)][github-markdownlint]
[![commitlint](https://img.shields.io/badge/commitlint-F7B93E?logo=c&logoColor=000&style=flat)][github-commitlint]
[![semantic-release](https://img.shields.io/badge/semantic--release-494949?logo=semanticrelease&logoColor=fff&style=flat)][github-semantic-release]
[![Shields.io](https://img.shields.io/badge/Shields.io-000?logo=shieldsdotio&logoColor=fff&style=flat)][shields]
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=flat)][git-scm]
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)][github]
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=fff&style=flat)][github-actions]
<!-- markdownlint-enable MD013 -->

## ✍️ Contributing

👍🎉 *First off, thanks for taking the time to contribute!* 🎉👍

Contributions are what make the open source community such an amazing place to
be learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

1. Fork the *Project*
2. Create your *Feature Branch* (`git checkout -b feature/awesome-feature`)
3. Commit your *Changes* (`git commit -m 'Add awesome feature'`)
4. Push to the *Branch* (`git push origin feature/awesome-feature`)
5. Open a *Pull Request*

## 💖 Like this project?

Leave a ⭐ if you think this project is cool or useful for you.

## ⚠️ License

`raid` is licenced under the MIT License. See the [LICENSE](LICENSE)
for more information.

<!-- markdownlint-disable MD013 -->
<!-- Github links -->
[github-actions]: https://docs.github.com/en/actions
[github-bandit]: https://github.com/PyCQA/bandit
[github-black]: https://github.com/psf/black
[github-commitlint]: https://github.com/conventional-changelog/commitlint
[github-flake8]: https://github.com/PyCQA/flake8
[github-markdownlint]: https://github.com/DavidAnson/markdownlint
[github-pre-commit]: https://github.com/pre-commit/pre-commit
[github-semantic-release]: https://github.com/semantic-release/semantic-release
[github-typer]: https://github.com/tiangolo/typer
[github]: https://github.com

<!-- Other links -->
[editorconfig]: https://editorconfig.org
[git-scm]: https://git-scm.com
[shields]: https://shields.io
[slack-api-users-list]: https://api.slack.com/methods/users.list
[telegram-air-alert-ua]: https://telegram.me/air_alert_ua
[telegram-api]: https://core.telegram.org/api
