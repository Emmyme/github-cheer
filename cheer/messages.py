
def get_message(commits_today, commits_week):
    if commits_today >= 3:
        return  f" Wow! {commits_today} commits today! Keep crushing it!"
    elif commits_week >= 10:
        return f" You made {commits_week} commits this week! You're on fire!"
    else:
        return f"Good job! You made {commits_today} commits today and {commits_week} commits this week. Keep it up!"
    