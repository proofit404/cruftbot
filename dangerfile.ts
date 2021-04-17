export default async (): undefined => {
  if (!/^[A-Z]/.test(danger.github.pr.title)) {
    fail("Pull request title should start with capital letter.");
    return;
  }
// @todo #92 Issue title should start with capital letter.
// @todo #92 Commit message should start with capital letter.
  if (!/\.$/.test(danger.github.pr.title)) {
    fail("Pull request title should ends with the dot.");
    return;
  }
// @todo #92 Issue title should ends with the dot.
// @todo #92 Commit message should ends with the dot.

// @todo #92 Commit title SHOULD contain issue number.
// @todo #92 Pull request title SHOULD NOT contain issue number.
// @todo #92 Pull request body SHOULD contain issue number.

// @todo #92 Multiline commit message should separate title with new line.

  if (danger.github.pr.labels.length > 0) {
    fail("Pull request should not have labels.");
    return;
  }
// @todo #92 Issue should not have labels.
};
