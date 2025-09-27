
import random

def get_message(commits_today, commits_week):
    if commits_today >= 8:
        return random.choice([
            f" Incredible! {commits_today} commits today! You're absolutely crushing it!",
            f" Holy commits! {commits_today} today - you're on fire!",
            f" {commits_today} commits today?! That's some serious dedication!"
        ])
    
    elif commits_today >= 5:
        return random.choice([
            f" Amazing! {commits_today} commits today! You're in the zone!",
            f" Wow! {commits_today} commits today - fantastic momentum!",
            f" {commits_today} commits today! You're really hitting your stride!"
        ])
    
    elif commits_today >= 3:
        return random.choice([
            f" Excellent! {commits_today} commits today! Keep crushing it!",
            f" Great work! {commits_today} commits today - solid progress!",
            f" Nice! {commits_today} commits today! You're building momentum!"
        ])
    
    elif commits_week >= 25:
        return random.choice([
            f" Outstanding! {commits_week} commits this week! You're unstoppable!",
            f" Phenomenal! {commits_week} commits this week - legendary work!",
            f" {commits_week} commits this week?! Absolutely incredible dedication!"
        ])
    
    elif commits_week >= 15:
        return random.choice([
            f" Impressive! {commits_week} commits this week! You're unstoppable!",
            f" Strong week! {commits_week} commits - excellent consistency!",
            f" {commits_week} commits this week! You're really in your element!"
        ])
    
    elif commits_week >= 10:
        return random.choice([
            f" Great week! {commits_week} commits! You're on fire!",
            f" Nice work! {commits_week} commits this week - keep it rolling!",
            f" {commits_week} commits this week! Solid rhythm you've got there!"
        ])
    
    elif commits_today == 0 and commits_week > 0:
        return random.choice([
            f" {commits_week} commits this week so far. Ready for today's first?",
            f" You've got {commits_week} this week already. Time to add one more?",
            f" {commits_week} commits this week! Ready to keep the streak going?"
        ])
    
    elif commits_today == 0 and commits_week == 0:
        return random.choice([
            " Fresh start! Ready to make your first commit of the week?",
            " New week, new opportunities! Let's get coding!",
            " Time to get those commits flowing! Every journey starts with one."
        ])
    
    elif commits_today == 1:
        return random.choice([
            f" Nice start! 1 commit today, {commits_week} this week. Keep building!",
            f" Good momentum! 1 today brings your week to {commits_week}!",
            f" Great! 1 commit today - every commit counts toward your {commits_week} this week!"
        ])
    
    elif commits_today == 2:
        return random.choice([
            f" Solid! 2 commits today and {commits_week} this week. Nice pace!",
            f" Good rhythm! 2 today, {commits_week} total this week!",
            f" Building up! 2 commits today - you're finding your groove!"
        ])
    
    else:
        return random.choice([
            f" Good work! {commits_today} commits today and {commits_week} this week. Keep it up!",
            f" Nice progress! {commits_today} today, {commits_week} this week - steady as she goes!",
            f" Consistent effort! {commits_today} commits today, {commits_week} total this week!"
        ])
    