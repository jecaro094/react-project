## react-project

System to track pokemons stats using [pokeapi public API](https://github.com/jecaro094/react-project/edit/main/README.md) as external service.

Used react for dashboards creation, and fastapi for backend system.

Pokedex data available:

<img width="1858" height="890" alt="Screenshot 2025-12-21 at 16 48 24" src="https://github.com/user-attachments/assets/b0a31bdf-ca7f-4074-97ab-fa617e659edc" />

Select pokemon for further info:

<img width="997" height="839" alt="Screenshot 2025-12-21 at 16 44 26" src="https://github.com/user-attachments/assets/9298aa8e-4e32-444f-9154-9d826388776e" />

## Current state of the app (03-08-2024)

- I can run the app locally running `docker-compose up --build`, from the root of the repo.
- I can deploy the app to `eb aws` following these steps:
	- Create `Test-env` as aws elastic beanstalk environment (docker).
	- Configure the environment, from terminal, to accept `ssh` connection.
		- `eb ssh Test-env`
		- The environment will restart to apply the changes.
	- Run github workflow `db-workflow.yaml`, manually from `react-project` repo on github.
	- Connect `eb ssh Test-env` to check that all 4 containers are running with `sudo docker ps`
	- If necessary, run `sudo docker logs <CONTAINER_ID>` to check the log from the deployed container(s).
	- Check that you can access the login from the new eb environment `url`

## CONSIDERATIONS TO RUN ON LOCAL
- Switch from `named volume` to `bind volume`, in the `db` docker service.
	- Do it in order to consider the data that is in this repo, for postgres, but that is not commited in git.
	- Location: `./backend/db_data`
- I won't put the saved data from the database (`backup.sql`) in the github project, but I will let it defined on my Mac, without committing it.
	- I don't do it for security reasons.
- The `.env` file that I consider when I run the app locally with docker, is on my Mac too. I do not commit the file for security reasons.

## CONSIDERED IN ORDER TO DEPLOY ON AWS (TO MAKE IT WORK)
- Define github environment variables (**DONE**)
- The workflow considered for deployment is `db-workflow.yaml`
	- We do not need the `ECR` registry for docker anymore, so I can delete it anytime in the future. So that I save some money.
	- The deployment from the `yaml` is `manual` on github.

## TODO AFTER DEPLOY ON AWS
- Put data on `database` in the remote server deployed on `AWS`. 
    - Use a `named volume` so that the data persists, without depending on docker container restarts.
		- Remember to edit the `docker-compose.yaml` file so that it matches this config.
    - Use `transfer_db.sh`, following the instructions detailed below.


## TODO IN THE FUTURE
- Include `https` over `http`. Otherwise, this won't work on `chrome`, due to restrictions on the cookies (cookies that I define in the frontend).
- Fix case sensitivity when looking for pokemon in the search bar.
- Make the app responsive for mobile too.

## How to import data to the database in the deployment server (in AWS)

Remember to give execution permissions to the database shell script, just like this:

```bash
chmod +x transfer_db.sh
```

And then, you can run the script replacing your variables of interest:

```bash
./transfer_db.sh <LOCAL_DB_USER> <LOCAL_DB_NAME> <LOCAL_DB_HOST> <SSH_KEY_PATH> <EC2_USER> <EC2_HOST> <POSTGRES_EC2_USER> <POSTGRES_EC2_DB> 
```

If the script does not work, try to execute the instructions detailed in the file `transfer_db.sh`, step by step.
