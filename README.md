<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/logspace-ai/df2streamlit">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">df2streamlit</h3>

  <p align="center">
Convert Pandas DataFrame into Streamlit forms.
    <br />
    <a href="https://github.com/logspace-ai/df2streamlit"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/logspace-ai/df2streamlit">View Demo</a>
    ·
    <a href="https://github.com/logspace-ai/df2streamlit/issues">Report Bug</a>
    ·
    <a href="https://github.com/logspace-ai/df2streamlit/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This module helps you create Streamlit forms from DataFrame rows. Using a template to build column names you can define the form layout.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* Streamlit
* Pandas

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can run `streamlit run df2streamlit.py` to see it working.

### Prerequisites

* poetry
  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```

### Installation

Run `poetry install` to install the dependencies.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Basically, you define a dataframe with the columns you want to display in the form with the following format: `field_name.element_type.streamlit_column` (e.g `Class.selectbox.2`). This would create a selectbox with the unique values of the column `Class` and add that to the column `2` in the form, according to Streamlit layout.

This is still in development.

<p align="right">(<a href="#top">back to top</a>)</p>


See the [open issues](https://github.com/logspace-ai/df2streamlit/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/logspace-ai/df2streamlit.svg?style=for-the-badge
[contributors-url]: https://github.com/logspace-ai/df2streamlit/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/logspace-ai/df2streamlit.svg?style=for-the-badge
[forks-url]: https://github.com/logspace-ai/df2streamlit/network/members
[stars-shield]: https://img.shields.io/github/stars/logspace-ai/df2streamlit.svg?style=for-the-badge
[stars-url]: https://github.com/logspace-ai/df2streamlit/stargazers
[issues-shield]: https://img.shields.io/github/issues/logspace-ai/df2streamlit.svg?style=for-the-badge
[issues-url]: https://github.com/logspace-ai/df2streamlit/issues
[license-shield]: https://img.shields.io/github/license/logspace-ai/df2streamlit.svg?style=for-the-badge
[license-url]: https://github.com/logspace-ai/df2streamlit/blob/master/LICENSE.txt
