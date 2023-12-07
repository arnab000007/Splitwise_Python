
# Schema Design

### Table: **User**

| Column Name  | Data Type | Primary Key | Foreign Key |
| ------------ | --------- | ----------- | ----------- |
| id  | INT  | Yes | |
| name  | Varchar(255)  | | |
| phone_number  | Varchar(50)  | | |
| password  | Varchar(255)  |  | |
| created_at  | DateTime  |  | |
| last_modified  | DateTime  |  | |


### Table: **Group**

| Column Name  | Data Type | Primary Key | Foreign Key |
| ------------ | --------- | ----------- | ----------- |
| id  | INT  | Yes | |
| name  | Varchar(255)  | | |
| created_by_user_id  | INT  | | Yes |
| created_at  | DateTime  |  | |
| last_modified  | DateTime  |  | |



### Table: **GroupMembers**

| Column Name  | Data Type | Primary Key | Foreign Key |
| ------------ | --------- | ----------- | ----------- |
| id  | INT  | Yes | |
| group_id  | INT  | | Yes |
| member_user_id  | INT  | | Yes |
| created_at  | DateTime  |  | |
| last_modified  | DateTime  |  | |



### Table: **Expenses**

| Column Name  | Data Type | Primary Key | Foreign Key |
| ------------ | --------- | ----------- | ----------- |
| id  | INT  | Yes | |
| group_id  | INT  | | Yes |
| is_group_expense  | BIT  | |  |
| paid_by_user_id  | INT  | | Yes |
| paid_amount  | FLOAT  | |  |
| created_at  | DateTime  |  | |
| last_modified  | DateTime  |  | |

### Table: **ExpenseSplits**

| Column Name  | Data Type | Primary Key | Foreign Key |
| ------------ | --------- | ----------- | ----------- |
| id  | INT  | Yes | |
| expense_id  | INT  | | Yes |
| user_id  | INT  | |  Yes |
| split_amount  | FLOAT  | | |
| created_at  | DateTime  |  | |
| last_modified  | DateTime  |  | |


### Table: **Transactions**

| Column Name  | Data Type | Primary Key | Foreign Key |
| ------------ | --------- | ----------- | ----------- |
| id  | INT  | Yes | |
| group_id  | INT  | | Yes |
| is_group_transaction  | BIT  | |  |
| received_by_user_id  | INT  | |  Yes |
| paid_by_user_id  | INT  | |  Yes |
| amount  | FLOAT  | | |
| is_settled  | BIT  | |  |
| created_at  | DateTime  |  | |
| last_modified  | DateTime  |  | |