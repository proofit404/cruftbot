export default async (): undefined => {
  const pullRequestTest = danger.github.pr.body.match(/^#(\d+)$/);

  if (!pullRequestTest) {
    fail("Pull request body SHOULD contain issue number.");
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

  // @todo #92 Commit message should start with capital letter.

  if (!/\.$/.test(danger.github.pr.title)) {
    fail("Pull request title should ends with the dot.");
    return;
  }

  if (!isBotIssue && !/\.$/.test(issueJSON.data.title)) {
    fail("Issue title should ends with the dot.");
    return;
  }

  // @todo #92 Commit message should ends with the dot.

  // @todo #92 Commit title SHOULD contain issue number.

  // @todo #92 Pull request title SHOULD NOT contain issue number.

  // @todo #92 Multiline commit message should separate title with new line.

  if (danger.github.pr.labels.length > 0) {
    fail("Pull request should not have labels.");
    return;
  }

  if (issueJSON.data.labels.length > 0) {
    fail("Issue should not have labels.");
    return;
  }
};
