export default async (): undefined => {
  const isBotPullRequest = danger.github.pr.user.login === "dependabot[bot]";

  if (isBotPullRequest) {
    message("Ignore review of automatic pull requests.");
    return;
  }

  const pullRequestTest = danger.github.pr.body.match(/^#(\d+)$/);

  if (!pullRequestTest) {
    fail("Pull request body should contain issue number.");
    return;
  }

  const issueNumber = pullRequestTest[1];

  const issueJSON = await danger.github.api.issues.get({
    owner: danger.github.thisPR.owner,
    repo: danger.github.thisPR.repo,
    issue_number: parseInt(issueNumber),
  });

  if (issueJSON.status !== 200) {
    fail(`Unable to check issue #${issueNumber}`);
    return;
  }

  const isBotIssue = issueJSON.data.user.login === "0pdd";

  if (!/^[A-Z]/.test(danger.github.pr.title)) {
    fail("Pull request title should start with capital letter.");
    return;
  }

  if (!isBotIssue && !/^[A-Z]/.test(issueJSON.data.title)) {
    fail("Issue title should start with capital letter.");
    return;
  }

  for (const commit of danger.git.commits) {
    if (!/^[A-Z]/.test(commit.message)) {
      fail("Commit message should start with capital letter.");
      return;
    }
  }

  if (!/\.$/.test(danger.github.pr.title)) {
    fail("Pull request title should ends with the dot.");
    return;
  }

  if (!isBotIssue && !/\.$/.test(issueJSON.data.title)) {
    fail("Issue title should ends with the dot.");
    return;
  }

  for (const commit of danger.git.commits) {
    if (!/\.$/.test(commit.message)) {
      fail("Commit message should ends with the dot.");
      return;
    }
  }

  for (const commit of danger.git.commits) {
    if (!commit.message.split(/\r?\n/)[0].endsWith(` (#${issueNumber}).`)) {
      fail("Commit title should contain issue number.");
      return;
    }
  }

  for (const commit of danger.git.commits) {
    const commitLines = commit.message.split(/\r?\n/);
    if (commitLines.length > 1 && commitLines[1] !== "") {
      fail("Multiline commit message should separate title with new line.");
      return;
    }
  }

  if (danger.github.pr.title.includes(`#${issueNumber}`)) {
    fail("Pull request title should not contain issue number.");
    return;
  }

  if (danger.github.pr.labels.length > 0) {
    fail("Pull request should not have labels.");
    return;
  }

  if (issueJSON.data.labels.length > 0) {
    fail("Issue should not have labels.");
    return;
  }
};
