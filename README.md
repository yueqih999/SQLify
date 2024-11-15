# SQLify

Welcome to SQLify! Below is a screenshot of the SQLify interface:

![SQLify Webpage](data/webpage.png "SQLify Webpage")

### Website
Access SQLify at [SQLify Chat](https://sqlify-chat.vercel.app/).

### Inspiration
With the growing need to interact with databases through natural language, we saw an opportunity to bridge the gap between users and data by creating a chatbot that interprets plain language prompts into SQL queries. 
This project aims to simplify data access for non-technical users, allowing them to obtain the data insights they need without requiring SQL knowledge.

### What it does
SQLify is an AI-driven chatbot fine-tuned on GPT-4o, designed to convert user prompts into accurate SQL queries. Users can simply ask questions or make requests in natural language, and SQLify translates these prompts into SQL commands, enabling seamless data interaction for anyone, regardless of technical expertise.

### How we built it
We built SQLify by fine-tuning GPT-4o, leveraging a dataset of natural language prompts paired with their respective SQL queries. The model was trained to recognize patterns and structures in user prompts to accurately generate SQL syntax. The backend was implemented to handle database connections and execute generated SQL, providing users with immediate query results.

#### Model Performance
Below is the model performance plot that illustrates the training and validation loss, alongside the token accuracy over training steps:

![Model Performance](data/Metrics.png "Model Fine-Tune Metrics")

### Challenges we ran into
- **Model Fine-Tuning**: Fine-tuning GPT-4o to balance natural language understanding with SQL accuracy required extensive experimentation with hyperparameters and batch sizes to avoid overfitting or underfitting.
- **Error Handling**: Since SQL queries generated by the model can vary widely in complexity, ensuring proper error handling and validation for different databases posed a unique challenge.

### 👉 Run it locally 

> **Step 1** - Once the project is downloaded, change the directory to `web-app`. 

```bash
$ cd web-app
```

<br >

> **Step 2** - Install dependencies

```bash
$ nvm install 16
$ nvm use 16
$ npm i
$ pip install -r requirements.txt
```

<br />

> **Step 3** - Start in development mode

```bash
$ flask run
```

<br />

At this point, the app is available in the browser `localhost:3000` (the default address).


### 👉 Codebase Structure

```bash
< ROOT  >
    |
   web-app/
    ├── templates
    │   ├── index.html
    │   ├── response.html
    ├── requirements.txt
    ├── app.py
    └── flight_database.db
    |
   data/
```

<br />


