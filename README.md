# Where Will I be Happy Next?
An analysis of the happiness score and how different categories may affect the happiness of a person.
## ECE 143 Team 14
**Achyut Pillai : A16646336\
Alexis Yu : A16323533\
Dominique Hernandez : A16659057\
Riya Joshi : A59023015\
Tripti Chanda : A59015561**

## Main Third-Party Libraries Used
- pandas
- numpy
- plotly
- matplotlib
- pycountry
- pycountry_convert
- seaborn
- scikit-learn
- country_converter
- kaleido
- openpyxl


## How to Run
1. Download the repo in your preferred location
2. Run the following command in your terminal/command prompt to install all neccessary libraries.
    ```bash
    pip install -r requirements.txt
    ```
    Similarly, install all libraries in requirements.txt if using the Jupyter Notebook.
3. All .py files will now be executable.

## File Structure
- All datasets used are stored within the data directory separated by categories.
- The images used in the presentation can also be found in the images folder
- All of the executable .py files are located in the root directory along with the Jupyter notebook, requirements.txt, and a pdf of the presentation slides.

```
├── data
│   └── folders of dataset separated by category
│       └── .csv/.xlsx files
├── images
│   └── folders of images separated by category
│       └── .png/.html files
├── requirements.txt
├── ...
├── .py files
├── ...
├── ECE 143 - Final Plots.ipynb
└── PDF of Presentation slides
```