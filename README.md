# Pandas LeetCode Solutions

A collection of solutions to **LeetCode database and data manipulation problems** implemented using **Pandas** and **SQL**.

This repository focuses on solving problems that involve tabular data manipulation, filtering, grouping, joins, and aggregation — tasks that closely resemble real-world data analysis workflows.

The goal of this repository is to practice and demonstrate **data transformation techniques using Pandas**, while also comparing them with their **SQL equivalents**.

---

## Repository Structure

```
pandas-leetcode-solutions
│
├── problems
│ ├── 001_duplicate_emails
│ │ ├── pandas_solution.py
│ │ ├── sql_solution.sql
│ │ ├── alt_solution.py (optional)
│ │ └── notes.md
│ │
│ ├── 002_second_highest_salary
│ │ ├── pandas_solution.py
│ │ ├── sql_solution.sql
│ │ └── notes.md
│ │
│ └── ...
│
└── README.md
```

Each problem is organized into its own folder and typically contains:

- **pandas_solution.py** – solution implemented using Pandas
- **sql_solution.sql** – equivalent SQL query
- **alt_solution.py** *(optional)* – an alternative approach
- **notes.md** – explanation of the logic and approach

---

## Objectives

This repository is designed to practice and demonstrate:

- Data manipulation with **Pandas**
- SQL query design and translation to Pandas
- Aggregations and group operations
- Filtering and conditional logic
- Data joins and merges
- Understanding tabular data problems

Many LeetCode database problems mirror real-world analytics tasks, making them useful exercises for developing **data analysis and data engineering skills**.

---

## Problem Categories

The problems solved in this repository cover common data operations such as:

- Filtering rows based on conditions
- Identifying duplicates
- Aggregations and grouping
- Ranking and ordering
- Joins across tables
- Conditional transformations

---

## Example Problem

### Duplicate Emails

Find all duplicate email addresses in a table.

#### SQL Solution

```sql
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

Pandas Solution

```
df[df.duplicated("email", keep=False)]["email"].drop_duplicates()
```

---

## Why Pandas + SQL
```Many real-world data problems can be solved using either SQL queries or Pandas transformations.```

This repository helps build intuition for:

- Translating SQL logic into Pandas operations
- Understanding when to use grouping, filtering, and joins
- Practicing common analytical data operations

---

## Learning Outcomes

Working through these problems helps develop skills in:
- Data manipulation
- Analytical thinking
- Query optimization
- Understanding relational data structures
- Implementing SQL-like logic using Python

---

## Future Improvements

Possible additions to this repository include:
- More LeetCode problems
- Performance comparisons between SQL and Pandas
- Additional alternative solutions
- Notebook-based walkthroughs

---

## Author

**Jayesh Suryawanshi**
Data Analyst / Analytics Engineering
GitHub: https://github.com/TheJayesh25

--- 

## LICENSE
MIT License - For learning and educational purposes