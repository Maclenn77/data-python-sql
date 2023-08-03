# README

## Video Data Extraction and Reporting App

This Python application is designed to extract video data from a directory called `video_clips`, store the data in a PostgreSQL database, and generate a CSV report. Please follow the instructions provided below to successfully use this application.

### Prerequisites

- Python 3.x installed on your system
- PostgreSQL installed on your system
- Video files available in the `video_clips` directory

### Installation

1. Clone this repository to your local machine or download the source code.
2. Ensure that all the required Python packages are installed by executing the following command in your terminal:

```shell
pip install -r requirements.txt
```

3. Create a copy of the `.env-template` file and rename it to `.env` by executing the following command in your terminal:

```shell
cp .env-template .env
```

4. Open the newly created `.env` file using a text editor and provide the necessary details for the database connection. Update the following placeholders with your database connection information:

```
HOSTNAME=<your_database_host>
PORT=<your_database_port>
DATABASE=<your_database_name>
USERNAME=<your_database_user>
PASSWORD=<your_database_password>
```

### Usage

1. Place your video files inside the `video_clips` directory created by the Python application.

2. Run the application by executing the following command in your terminal:

```shell
python main.py
```

3. The application will automatically extract video data from the `video_clips` directory, store the data in the specified PostgreSQL database, and generate a CSV report.

4. Once the process is complete, you will find the generated CSV report in the report directory with the name `video_clips.csv`.

### Troubleshooting

- If you encounter any issues or errors during the application execution, please ensure that you have provided the correct database connection information in the `.env` file.

- Make sure the video files are correctly placed inside the `video_clips` directory and have the required file extensions for video files.

### License

This project is licensed under the [MIT license](LICENSE).

### Contributions

Contributions to this project are always welcome! If you have any improvements, suggestions, or bug fixes, please feel free to open a pull request or submit an issue.
