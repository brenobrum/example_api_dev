# What is this repo for?

This repo is a POC of how we can develop better with LLM's faster.


## The problem

This repo is a simple API for movies

Each movie has an author and a genre.

In this first step, the only thing that is implemented is the api for creating a genre.

`POST /api/genre`

We are implementing this with a DDD aproach.

The application layer has all the routes, and each of the route has its usecases.

If we were to implement a new endpoint by hand, lets say, `GET /api/genre/:id`, to retreve the genre we've just created, it would take some time.

But we can use help from tools like Cursor or Claude Code to implement a new route for us.

But somethimes the result is not as we want, and if not made with care it can lead to a mess in the future.

One of the ways we could do it, is by add rules for the agents, or simpler, a agents.md that has all the best practices to implement a new endpoint in our API.

This is well know already, and its the way we been doing stuff for a while.

But doing it like this can also be expansive and time consuming, as the agent will need to create every folder and file for the test, usecases, routes, models, etc.

But I think we can make it cheapper and faster.

## Doing stuff as in the old days

As in the old days, when we did not have LLM's, a good approach for creating new modules without having to write everything over and over again, was with scaffolds.

As you might know, a scaffold is a script that creates a template of something for you.

What if, instead of asking for the LLM to create every file and folder every single time, it just created a script that yould do that for it.

The agent would just need to update the code in the files, if needed.

## Implementing

### 1 - Planning
Instead of doing it by hand, we are going to ask the agent create the script for us.

How are we going to do that?

The first step is to make the agent learn our current code structure.

Prompt:

```prompt
Read trought the file structure of this repo, inside /app.

Understand how each part the structure work, how they connect to one another, how changing one may cause a change at another one.

After that, create a modules_connections.md file that contains the connections of each of that modules.

Ensure to explain clearly and with every detail how each of the files of each module are created and best practices 
```

### 2 - Implementing
After running the prompt, modules_connections.md file was created, now we run the following prompt

```prompt
Inside /scaffold, for each of the modules, create a script that can scaffold a complete module in the app.

Make sure to create the scaffold scripts for each of the little parts, those little parts will be used to create bigger parts.

Example:
CreateRoute
CreateUseCase
CreateModel
CreateDomainRepository
CreateInfraRepository

When a user wants to create a full api module, the scaffold needs to create every usecase, route, model, domain repository and infra repository.

But if the user whants to just add a new use case, the scaffolds will only create the usecase in the already existing module, with its tests and everything, and append that to the routes file.

Also, add a compreensive gide on how to use that scaffold system to other agents, inside agents.md, ensure to set a instruction to always use the module scaffold system when creating something new.

The agent will use the scaffold system to create new things, and just update the code with the specifics of the implementation.
```

### 3 - Running

After the agent created all the scripts inside /scaffold, we can now try to implement our new endpoint:

`GET /api/genre/:id`

```prompt
Create a new route for genre, it should get the creted genre by id
```

Just as that, the agent run and created the full route, working, and running, as you can see in app/application/api/genres/use_cases/get_genre, not allucinations, no linting erros, ultra fast because the model didn't had to create every file with tool calls.

But why stop there, why don't we ask the agent to implement the full genre CRUD.

```prompt
Implement the rest of the CRUD for genre.
```

And now, the full CRUD is flowlessly implemented.

We can go even further, lets run it to create a new module, the authors module.

```prompt
Implement the author module.
```

Just as that, we have a fully working implementation of the authors module. With every route and usecase, but not only that, it has all the domain and infra files too, and its tested.

Just to finish the POC, lets run it for the movies modules.

```prompt
Implement the movies module.
```

And everything is working as it should.

## Why is that powerfull

As I was documenting each of the steps, I did it module by module, but we could had done more then that, we could had made all 3 modules at once, and it would be way faster than just having the agent whiting everything by hand.

Whiting code with agents is faster than doing it by hand, but it can lead to erros or inconsistancy in the long run, but LLM's are not faster than actual code.

The LLM's are still needed to write the code for us, but it can focus on the code, and not in the file structure or the code structure.

This makes the process way faster and secure keeping consistency.