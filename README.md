# Plaid_Django_App-master

1) User signup, login, logout APIs.
2) Token exchange API: An authenticated user can submit a plaid public token that he gets post link integration.
3) This public token is exchanged for access token on the backend.
4) This initiates an async job on the backend for fetching account and item metadata for the access token.
5) Expose a webhook for handling plaid transaction updates and fetch the transactions on receival of a webhook.
6) Expose an api endpoint for fetching all transaction and account data each for a user.
7) Do appropriate plaid error handling.


<h2>Prerequisites</h2>
<p>You will need API keys</p>
<code>https://dashboard.plaid.com/team/keys</code>

<h2>Installing</h2>
<h4>Open terminal in project folder to create and run virtual environment</h4>
<code>python -m venv ./venv</code><br>
<code>venv\scripts\activate.bat</code><br>

<h2>Create a database and write the credentials in settings.py file of moneymanager app</h2>

<h2>Now make migrations</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>Enter the Plaid API credentials in secret_keys.py file</h2>
<pre>
PLAID_CLIENT_ID = 'YOUR CLIENT ID'
PLAID_ENV = 'PLAID ENVIRONMENT'
PLAID_SECRET = 'YOUR SECRET KEY'
</pre>

<h2> To run the program in local server use the following command</h2>
<code>python manage.py runserver</code>
