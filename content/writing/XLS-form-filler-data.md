Title: Introducing XLSform filler data
Date: 2023-07-22 18:35
Modified: 2023-07-22 18:35
Tags: analysis, python, xlsform, kobo, software
Category: General
Slug: XLSform-filler-data
Author: Brian
Status: published
Summary: A tool for creating sample data for testing and drafting analysis-plans. 

## The Problem

Analysis tools such as Python and R provide many benefits for humanitarian analysis. They provide reproducible analysis flows which are great for collaborative analysis, provide an approach than can build reuse and build upon prior analysis and importantly, provide an auditable, robust and reproducible approach. 

Another of their strengths is how it enables faster turn-around on analytical products due to its reuse of code and methods. This is the case in situations where the analytical product design remains very close to previous examples, but what about the many cases cases where the output analysis needs to be adjusted to fit the context or a new methodology or mix of methods. In these cases one of the most limiting factors in the analysis turnaround time is the period where the analyst needs to wait for data inputs or produce example data in order to start developing their data analysis plan or draft their analysis. 

A tool that can simulate data can radically reduce the time between data collection and the production date of its analytical outputs. 

## A Solution

That's what *XLSform filler data* aim to accomplish. Using as an input, an XLSform survey, the tool creates a sample survey dataset which can be used in generating a analysis plan and drafting of the initial analysis, allowing the analyst to prepare the descriptive analysis sections in advance of the data collection period, freeing the analyst up to focus on the higher levels of the analysis spectrum, the explanations, the interpretations, the anticipations and the prescriptions. 

The tool is written in and is focused on the Python ecosystem. its published on PyPi and can be installed with the following command ```pip install XLSform-data-filler```.

## Usage
To create a dummy dataset, with a default number of rows(100) from a XLSform source: ```xlsform-filler-data <source-file-path>/<filename.xlsx>```
To specify the number of rows to create, use the -r flag. Example: ```xlsform-filler-data <source-file-path>/<filename.xlsx> -r 200```
To specify the output path and filename, pass the -o flag. Example: ```xlsform-filler-data <source-file-path>/<filename.xlsx> -o <./myfile.xlsx>```

## Roadmap
As of version 0.1.1 the tool does not properly randomise multiple choice questions; omits some variables such as 'start' and 'end'; does not maintain the order of the variables; and does not incorporate constraints or cascading choice lists. These limitations will be addressed in future releases.


