# API Lua 🌘

API to generate astrological charts using [Kerykeion](https://github.com/g-battaglia/kerykeion), a Python library for astrology that calculates planetary and house positions, detects aspects, and generates SVG charts, including natal, synastry, transit, and composite charts. The API also allows customization of which planets to include in the calculations and uses the full version of [Pyswisseph](https://github.com/astrorigin/pyswisseph), a Python implementation of the [Swiss Ephemeris](https://www.astro.com/swisseph/).

## Features ✨

- Generation of astrological charts in SVG format.
- Now, only support for natal chart. Coming soon support to synastry, transit, and composite charts.
- Customization of planets included in the calculations.
- Based on reliable libraries like Kerykeion and Pyswisseph.

## Requirements 📋

Make sure you have the following requirements installed:

- **Python 3.10.3**
- **Docker**

## Installation 🚀

1. Clone this repository:

   ```bash
   git clone https://github.com/andreideholte/api-lua.git
   cd api-lua
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application with Docker:

   ```bash
   docker build -t api-lua .
   docker run -p 5050:5050 api-lua
   ```

4. Access the API at `http://localhost:5050`.

## Usage 📖

The API provides endpoints to generate astrological charts. Examples of usage and detailed documentation can be found in the [Swagger](#swagger-documentation) file.

## Important Warning ⚠️

The `geonames_username` field used in the `def criarmapa()` function located in `app.py` is a personal username. You must create your own username for use. To do this, visit the [GeoNames website](https://www.geonames.org/) and register for a new username. This is required to ensure proper functionality of the API.

## License 📄

This project is licensed under the **GNU Affero General Public License v3**. See the [LICENSE](https://github.com/andreideholte/api-lua/blob/main/LICENSE) file for more details.

**Note:** The Swiss Ephemeris library is distributed under a dual licensing system: **GNU Affero General Public License** or **Swiss Ephemeris Professional License**. For more information, see the [libswe/LICENSE](https://github.com/astrorigin/swisseph/blob/696bda432298d482d27e67a0cf1238920301a7dd/LICENSE) file.

## Contributing 🤝

Contributions are welcome! Follow the steps below to contribute:

1. Fork the repository.
2. Create a branch for your feature or bug fix: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m 'Add my new feature'`.
4. Push to the remote repository: `git push origin my-feature`.
5. Open a Pull Request.

## Contact 📬

Created by [Andrei Nascimento](mailto:andreideholte@gmail.com). Feel free to get in touch!

---

Made with ❤️ by astrology enthusiasts.
