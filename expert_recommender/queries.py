developer_query = """
{
  user(login: "josepholasoji") {
    name
    email
    followers {
      totalCount
    }
    mycontributedprojects: repositories(first: 1, affiliations: COLLABORATOR) {
      nodes {
        name
        description
        createdAt
        forkCount
        hasProjectsEnabled
        isDisabled
        updatedAt
        commits: object(expression: "master") {
          ... on Commit {
            history(first: 100, author: {emails: ["josepholasoji@gmail.com"]}) {
              edges {
                node {
                  additions
                  deletions
                  comments {
                    totalCount
                  }
                  author {
                    email
                    name
                    date
                  }
                }
              }
              totalCount
            }
          }
        }
        releases {
          totalCount
        }
        primaryLanguage {
          name
        }
        languages(first: 100) {
          nodes {
            name
          }
        }
      }
    }
    myprojects: repositories(first: 2, affiliations: OWNER) {
      nodes {
        name
        description
        createdAt
        forkCount
        hasProjectsEnabled
        isDisabled
        updatedAt
        commits: object(expression: "master") {
          ... on Commit {
            history(first: 100, author: {emails: ["josepholasoji@gmail.com"]}) {
              edges {
                node {
                  additions
                  deletions
                  comments {
                    totalCount
                  }
                  author {
                    email
                    name
                    date
                  }
                }
              }
              totalCount
            }
          }
        }
        releases {
          totalCount
        }
        primaryLanguage {
          name
        }
        languages(first: 100) {
          nodes {
            name
          }
        }
      }
    }
  }
}

"""

