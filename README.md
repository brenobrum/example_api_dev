# What is this repo for?

This repo is a POC of how we can build faster and better with LLMs.

## The Problem

This repo is a simple API for movies.

Each movie has an author and a genre.

In this first step, the only implemented endpoint is the API for creating a genre.

`POST /api/genre`

We are implementing this with a DDD approach.

The application layer contains all routes, and each route has its own use cases.

If we were to implement a new endpoint by hand, for example `GET /api/genre/:id` to retrieve the genre we just created, it would take time.

But we can use tools like Cursor or Claude Code to help implement new routes.

Sometimes the result is not what we want, and if it is not done carefully, it can lead to a mess in the future.

One way to improve this is by adding rules for agents, or more simply, an `agents.md` file with best practices for implementing new endpoints in this API.

This approach is already well known, and it is how we have been doing things for a while.

However, doing it this way can still be expensive and time-consuming, because the agent needs to create every folder and file for tests, use cases, routes, models, and so on.

I think we can make it cheaper and faster.

## Doing Things the Old Way

Back when we did not have LLMs, a good way to create new modules without rewriting everything repeatedly was to use scaffolds.

As you might know, a scaffold is a script that generates a template for you.

What if, instead of asking the LLM to create every file and folder every time, we asked it to create a script that does that for us?

Then the agent would only need to update the generated code when needed.

## Implementing

### 1 - Planning

Instead of doing it by hand, we ask the agent to create the script for us.

How are we going to do that?

The first step is to make the agent learn our current code structure.

Prompt:

```prompt
Read through the file structure of this repo, inside /app.

Understand how each part of the structure works, how they connect to one another, and how changing one part may cause changes in another.

After that, create a modules_connections.md file that documents the connections between each module.

Ensure you explain clearly, in detail, how each file in each module is created, along with best practices.
```

### 2 - Implementing

After running the first prompt, `modules_connections.md` is created. Now we run the following prompt:

```prompt
Inside /scaffold, for each module, create a script that can scaffold a complete module in the app.

Make sure to create scaffold scripts for each small part. These small parts will be used to build bigger parts.

Example:
CreateRoute
CreateUseCase
CreateModel
CreateDomainRepository
CreateInfraRepository

When a user wants to create a full API module, the scaffold must create every use case, route, model, domain repository, and infra repository.

If the user only wants to add a new use case, the scaffold should create only that use case in the existing module, including its tests, and append it to the routes file.

Also, add a comprehensive guide for other agents on how to use that scaffold system in `agents.md`, and include an instruction to always use the module scaffold system when creating something new.

The agent will use the scaffold system to create new items, and then only update code with implementation-specific details.
```

### 3 - Running

After the agent creates all scripts inside `/scaffold`, we can try implementing a new endpoint:

`GET /api/genre/:id`

```prompt
Create a new route for genre. It should get the created genre by id.
```

Just like that, the agent runs and creates the full route. It works, as you can see in `app/application/api/genres/use_cases/get_genre`: no hallucinations, no linting errors, and very fast because the model did not need to create every file with tool calls.

But why stop there? Why not ask the agent to implement the full genre CRUD?

```prompt
Implement the rest of the CRUD for genre.
```

Now the full CRUD is implemented.

We can go further and use it to create a new module: the authors module.

```prompt
Implement the author module.
```

Just like that, we have a fully working implementation of the authors module, with every route and use case. It also includes all domain and infra files, and it is tested.

To finish the POC, let us run it for the movies module.

```prompt
Implement the movies module.
```

And everything works as it should.

## Why This Is Powerful

While documenting each step, I did it module by module. But we could do even more: we could build all three modules at once, and it would still be much faster than having the agent write everything by hand.

Writing code with agents is faster than doing it by hand, but it can lead to errors or inconsistency in the long run. LLMs are helpful, but they are not faster than reusable code generation itself.

LLMs are still needed to write code for us, but they can focus on implementation details instead of file and code structure.

This makes the process much faster and more secure while preserving consistency.