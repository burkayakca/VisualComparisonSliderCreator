# Image Slider Creator with Gradio

This repository provides a Python-based tool to generate a visual comparison slider for two images. It uses Gradio for creating a user-friendly interface, Leafmap for the comparison functionality, and BeautifulSoup for HTML customization.

## Features

- Compare two images interactively using a slider.
- Customize the slider's title, descriptions, and responsiveness.
- Generates an HTML file ready for use.
- Supports Turkish characters and flexible styling.

## Installation

To use this tool, ensure you have the following dependencies installed:

```bash
pip install gradio leafmap beautifulsoup4
```

## Usage

### Python Function

The `sliderCreator` function generates an HTML comparison slider with the following parameters:

```python
def sliderCreator(title, img1, img2, label1, label2, description=" ", filename="slider.html", starting_position=50, isResponsive=True):
```

#### Parameters:

- `title`: Title of the slider.
- `img1`: File path of the first image.
- `img2`: File path of the second image.
- `label1`: Label for the first image.
- `label2`: Label for the second image.
- `description`: A short description of the slider.
- `filename`: Name of the generated HTML file (default: `slider.html`).
- `starting_position`: Initial slider position (default: `50`).
- `isResponsive`: Makes the slider responsive (default: `True`).

### Gradio Interface

The `gr.Interface` provides an easy-to-use GUI for generating the slider.

#### Inputs:

1. **Title**: Text input for the slider's title.
2. **First Image**: Upload the first image file.
3. **Second Image**: Upload the second image file.
4. **First Image Label**: Label for the first image.
5. **Second Image Label**: Label for the second image.
6. **Description**: Text area for a brief explanation.

#### Outputs:

- **Downloadable HTML File**: The generated slider file.

## Running the Tool

Run the script to launch the Gradio interface:

```bash
python slider_creator.py
```

Once launched, follow the instructions on the Gradio interface to upload images, add labels, and generate the slider.

## Example Output

The tool generates an HTML file that looks like this:

- **Title**: Displays the slider's name at the top.
- **Slider**: Interactive comparison slider with labels for each image.
- **Description**: An optional explanation below the slider.

## Customization

The generated HTML file can be further customized:

- **Styling**: The `style` tag inside the `<head>` element adjusts fonts, margins, and layout.
- **Meta Tags**: Supports UTF-8 encoding for Turkish characters.

## Dependencies

- **Gradio**: For building the interactive interface.
- **Leafmap**: For creating the comparison slider.
- **BeautifulSoup**: For editing and styling the HTML output.

## License

This project is licensed under the MIT License. Feel free to use and modify it for your needs.

## Contributing

If you have suggestions or encounter issues, feel free to open an issue or a pull request.
