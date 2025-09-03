# Doctor's Basecode

This project is a desktop application that analyzes medical texts (in PDF format) to extract clinical entities. It uses the Apache cTAKES clinical text analysis system to identify entities like medications, symptoms, diseases, anatomical sites, and procedures.

## Features

*   **PDF to Text Conversion:** Converts uploaded PDF files into plain text using the CloudConvert API.
*   **Clinical Entity Extraction:** Identifies and categorizes clinical entities from the text using a cTAKES server.
*   **Entity Enrichment:** Enriches the extracted entities with additional information from:
    *   **SNOMED CT:** Retrieves standard medical terms and concepts.
    *   **Wikipedia:** Fetches descriptions and images.
    *   **PubMed:** Searches for and retrieves related medical articles.
*   **GUI:** A PyQt5-based graphical user interface for file upload, entity visualization, and information access.
*   **Data Storage:** Saves extracted data and summaries in JSON and text formats.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/Doctor-s-Basecode-UCL.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the application:
    ```bash
    python3 ctakes.py
    ```
2.  The application will open a window. Click "Choose file" to upload a PDF file.
3.  Optionally, you can check the "Download Articles" and "Wikipedia Descriptions" boxes to fetch additional information.
4.  Click "Run" to start the analysis.
5.  Once the analysis is complete, a new window will display the extracted entities, categorized into:
    *   Medicine
    *   Symptoms
    *   Anatomy
    *   Procedures
    *   Diseases/Disorders
6.  You can click on an entity to view its SNOMED code and click the "Wikipedia" or "Articles" buttons to view the fetched information.

## Project Structure

```
├── apis/
│   ├── cloudconvert_api.py
│   ├── entrez_api.py
│   ├── snomed_api.py
│   └── wikipedia_api.py
├── classes/
│   ├── entity_class.py
│   └── summary_class.py
├── data/
├── gui/
│   └── gui.py
├── tests/
├── ctakes.py
├── requirements.txt
└── README.md
```

*   `ctakes.py`: The main script that orchestrates the entire process.
*   `gui/gui.py`: Defines the PyQt5 GUI.
*   `apis/`: Modules for interacting with external APIs.
*   `classes/`: Contains the `Entity` and `Summary` classes.
*   `tests/`: Unit tests for the application.
*   `data/`: Directory for storing extracted data and summaries.

## Dependencies

The project uses the following libraries:

*   `requests`
*   `wikipedia`
*   `cloudconvert`
*   `PyQt5`
*   `package`

## APIs Used

*   [Apache cTAKES](https://ctakes.apache.org/)
*   [CloudConvert API](https://cloudconvert.com/api/v1)
*   [NCBI Entrez API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
*   [SNOMED CT Browser API](https://browser.ihtsdotools.org/)
*   [Wikipedia API](https://pypi.org/project/wikipedia/)

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.