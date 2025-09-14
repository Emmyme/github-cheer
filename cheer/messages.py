
def get_message(commits_today, commits_week):
    if commits_today >= 5:
        return f" Amazing! {commits_today} commits today! You're in the zone!"
    
    elif commits_today >= 3:
        return f" Wow! {commits_today} commits today! Keep crushing it!"
    
    elif commits_week >= 15:
        return f" You made {commits_week} commits this week! You're unstoppable!"
    
    elif commits_week >= 10:
        return f" You made {commits_week} commits this week! You're on fire!"
    
    elif commits_today == 0:
        return f" {commits_week} commits this week so far. Ready for today's first?"
    
    else:
        return f" Good job! You made {commits_today} commits today and {commits_week} commits this week. Keep it up!"
    