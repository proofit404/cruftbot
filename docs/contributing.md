# Contributing

Development process of the `cruftbot` application is based on several wellknown methodologies. We expect you to follow this methodologies precisely. Otherwise, don't expect your contribution to be merged into the upstream.

## Branching, tickets, and continuous integration

We follow [Puzzle Driven Development](http://www.yegor256.com/2009/03/04/pdd.html). All changes should be proposed in a form of pull request. All changes should be discussed in tickets before implementation. We expect pull request build to be green before we review pull request.

## Local development

We have setup [Docker Compose Project](https://docs.docker.com/compose/) together with [Scripts To Rule Them All](https://github.com/github/scripts-to-rule-them-all) pattern. Every procedure you want to run during development should be wrapped in the dedicated script. Compose project should be a self-contained environment appropriate to run all scripts available in the repository. Users should not be forced to install anything on their machines except docker. Continuous integration build and local development should use the same set of scripts.

### Script execution

We strongly suggest you to use `run` command instead of `up`. The main difference in this case would be ability to use debugger since standard input & output streams would be allocated properly.

First of all, you need to install dependencies on your machine.

```
docker-compose run --rm app ./scripts/install
```

You can verify your changes of the codebase follow our style guide.

```
docker-compose run --rm app ./scripts/check
```

If some problems could be fixed automatically, you can use this command to apply these fixes.

```
docker-compose run --rm app ./scripts/lint
```

All contribution should be covered with tests. You can run our test suite with this command.

```
docker-compose run --rm app ./scripts/test
```

You can run application locally.

```
docker-compose run --rm --service-ports app ./scripts/serve
```

If you need to make some changes in a ad-hoc way, you are able to use application console for that.

```
docker-compose run --rm app ./scripts/console
```

You can update our production environment with that command. This script should run automatically in the continuous integration environment. You are not expected to execute this script when things are operating normally.

```
docker-compose run --rm app ./scripts/deploy
```

If you need to write some documentation pages, it's better to check how it will look like.

```
docker-compose run --rm --service-ports app ./scripts/serve-docs
```

You can update documentation site with that command. This script should run automatically in the continuous integration environment. You are not expected to execute this script when things are operating normally.

```
docker-compose run --rm app ./scripts/deploy-docs
```
