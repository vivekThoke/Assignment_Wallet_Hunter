from flask import Flask, render_template, request
from code_file import get_user_hashtag_usage_trend
from code_file import get_bot_activity_tracker
from code_file import get_content_moderation_alerts
from code_file import get_poll_participation_rate
from code_file import get_message_deletion_statistics
import json


app = Flask(__name__)

analytics_data = {
    'user_hashtag_usage_trend': {'chart_type': 'line', 'data': get_user_hashtag_usage_trend(), 
    'title': 'User Hashtag Usage Trend', 'description': 'This chart shows the trend of hashtag usage by users over time.'}, 
    'bot_activity_tracker': {'chart_type': 'line', 'data': [10, 15, 20, 25, 30, 35, 40], 'title': 'Bot Activity Tracker', 'description': 'This chart tracks the activity of bots over time.'}, 
    'content_moderation_alerts': {'chart_type': 'bar', 'data': [5, 10, 15, 5, 20, 25, 30], 'title': 'Content Moderation Alerts', 'description': 'This chart shows the number of content moderation alerts over time.'}, 
    'poll_participation_rate': {'chart_type': 'line', 'data': [70, 65, 75, 80, 85, 90, 95], 'title': 'Poll Participation Rate', 'description': 'This chart shows the participation rate in polls over time.'}, 
    'message_deletion_statistics': {'chart_type': 'bar', 'data': [20, 15, 25, 30, 10, 5, 0], 'title': 'Message Deletion Statistics', 'description': 'This chart shows the statistics of message deletions over time.'}, 
    'event_attendance': {'chart_type': 'line', 'data': [50, 75, 100, 125, 150, 175, 200], 'title': 'Event Attendance', 'description': 'This chart shows the attendance of events over time.'}, 
    'call_participation': {'chart_type': 'bar', 'data': [30, 40, 50, 60, 70, 80, 90], 'title': 'Call Participation', 'description': 'This chart shows the participation in calls over time.'}, 
    'group_mention_tracker': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35], 'title': 'Group Mention Tracker', 'description': 'This chart tracks the mentions of groups over time.'}, 
    'scheduled_message_success_rate': {'chart_type': 'line', 'data': [90, 92, 89, 94, 87, 95, 96], 'title': 'Scheduled Message Success Rate', 'description': 'This chart shows the success rate of scheduled messages over time.'}, 
    'spam_detection_count': {'chart_type': 'line', 'data': [5, 3, 6, 2, 7, 4, 1], 'title': 'Spam Detection Count', 'description': 'This chart shows the count of spam detections over time.'}, 
    'read_receipts_analysis': {'chart_type': 'line', 'data': [150, 160, 170, 180, 190, 200, 210], 'title': 'Read Receipts Analysis', 'description': 'This chart analyzes the read receipts over time.'}, 
    'message_edit_history': {'chart_type': 'bar', 'data': [10, 12, 8, 15, 7, 13, 9], 'title': 'Message Edit History', 'description': 'This chart shows the history of message edits over time.'}, 
    'user_reported_issues': {'chart_type': 'line', 'data': [2, 5, 3, 4, 1, 6, 2], 'title': 'User Reported Issues', 'description': 'This chart shows the issues reported by users over time.'}, 
    'moderation_response_time': {'chart_type': 'bar', 'data': [5, 10, 15, 20, 25, 30, 35], 'title': 'Moderation Response Time', 'description': 'This chart shows the response time of moderation actions over time.'}, 
    'keyword_alerts': {'chart_type': 'line', 'data': [10, 9, 11, 14, 8, 12, 10], 'title': 'Keyword Alerts', 'description': 'This chart shows the alerts triggered by specific keywords over time.'}, 
    'group_profile_updates': {'chart_type': 'line', 'data': [1, 2, 1, 3, 0, 1, 2], 'title': 'Group Profile Updates', 'description': 'This chart shows the updates made to group profiles over time.'}, 
    'automated_moderation_actions': {'chart_type': 'bar', 'data': [5, 10, 15, 10, 5, 0, 5], 'title': 'Automated Moderation Actions', 'description': 'This chart shows the actions taken by automated moderation over time.'}, 
    'external_link_clicks': {'chart_type': 'line', 'data': [50, 60, 70, 80, 90, 100, 110], 'title': 'External Link Clicks', 'description': 'This chart shows the number of clicks on external links over time.'}, 
    'user_invites_tracker': {'chart_type': 'bar', 'data': [10, 15, 20, 25, 30, 35, 40], 'title': 'User Invites Tracker', 'description': 'This chart tracks the number of user invites over time.'}, 
    'group_announcement_reach': {'chart_type': 'bar', 'data': [100, 150, 200, 250, 300, 350, 400], 'title': 'Group Announcement Reach', 'description': 'This chart shows the reach of group announcements over time.'}, 
    'user_mention_count': {'chart_type': 'line', 'data': [20, 25, 30, 35, 40, 45, 50], 'title': 'User Mention Count', 'description': 'This chart shows the count of user mentions over time.'}, 
    'user_complaints_and_feedback': {'chart_type': 'bar', 'data': [5, 10, 15, 10, 5, 0, 5], 'title': 'User Complaints and Feedback', 'description': 'This chart shows the number of user complaints and feedback over time.'}, 
    'group_expense_tracking': {'chart_type': 'line', 'data': [100, 200, 300, 250, 350, 400, 450], 'title': 'Group Expense Tracking', 'description': 'This chart tracks the expenses of groups over time.'}, 
    'user_profile_picture_changes': {'chart_type': 'line', 'data': [5, 10, 5, 15, 10, 20, 15], 'title': 'User Profile Picture Changes', 'description': 'This chart shows the changes in user profile pictures over time.'}, 
    'message_flagging_for_review': {'chart_type': 'bar', 'data': [3, 6, 2, 5, 4, 7, 1], 'title': 'Message Flagging for Review', 'description': 'This chart shows the number of messages flagged for review over time.'}, 
    'user_onboarding_completion': {'chart_type': 'bar', 'data': [90, 85, 95, 80, 75, 70, 100], 'title': 'User Onboarding Completion', 'description': 'This chart shows the completion rate of user onboarding over time.'}, 
    'user_engagement_by_hour': {'chart_type': 'bar', 'data': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], 'title': 'User Engagement by Hour', 'description': 'This chart shows the engagement of users by hour.'}, 
    'group_announcement_effectiveness': {'chart_type': 'line', 'data': [80, 85, 90, 95, 100, 105, 110], 'title': 'Group Announcement Effectiveness', 'description': 'This chart shows the effectiveness of group announcements over time.'}, 
    'user_feedback_trend': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35], 'title': 'User Feedback Trend', 'description': 'This chart shows the trend of user feedback over time.'}, 
    'group_discussion_complexity': {'chart_type': 'line', 'data': [1.5, 1.7, 1.6, 1.8, 1.9, 2.0, 2.1], 'title': 'Group Discussion Complexity', 'description': 'This chart shows the complexity of group discussions over time.'}, 
    'group_mention_impact': {'chart_type': 'line', 'data': [10, 15, 20, 25, 30, 35, 40], 'title': 'Group Mention Impact', 'description': 'This chart shows the impact of group mentions over time.'}, 
    'user_satisfaction_ratings': {'chart_type': 'bar', 'data': [4.5, 4.7, 4.6, 4.8, 4.9, 5.0, 4.8], 'title': 'User Satisfaction Ratings', 'description': 'This chart shows the satisfaction ratings of users over time.'}, 
    'user_activity_patterns': {'chart_type': 'line', 'data': [10, 20, 30, 40, 50, 60, 70], 'title': 'User Activity Patterns', 'description': 'This chart shows the activity patterns of users over time.'}, 
    'group_content_moderation': {'chart_type': 'bar', 'data': [5, 10, 15, 20, 25, 30, 35], 'title': 'Group Content Moderation', 'description': 'This chart shows the moderation of group content over time.'}, 
    'user_invitation_conversion': {'chart_type': 'line', 'data': [50, 55, 60, 65, 70, 75, 80], 'title': 'User Invitation Conversion', 'description': 'This chart shows the conversion rate of user invitations over time.'}, 
    'user_message_edit_rate': {'chart_type': 'line', 'data': [5, 10, 15, 10, 5, 0, 5], 'title': 'User Message Edit Rate', 'description': 'This chart shows the rate of user message edits over time.'}, 
    'group_event_participation': {'chart_type': 'bar', 'data': [20, 40, 60, 80, 100, 120, 140], 'title': 'Group Event Participation', 'description': 'This chart shows the participation in group events over time.'}, 
    'group_notification_responses': {'chart_type': 'line', 'data': [10, 20, 30, 40, 50, 60, 70], 'title': 'Group Notification Responses', 'description': 'This chart shows the responses to group notifications over time.'}, 
    'group_keyword_tracking': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35], 'title': 'Group Keyword Tracking', 'description': 'This chart tracks the usage of keywords in groups over time.'}, 
    'group_fundraising_efforts': {'chart_type': 'line', 'data': [1000, 2000, 3000, 4000, 5000, 6000, 7000], 'title': 'Group Fundraising Efforts', 'description': 'This chart shows the fundraising efforts of groups over time.'}, 
    'user_mention_responses': {'chart_type': 'bar', 'data': [10, 20, 30, 40, 50, 60, 70], 'title': 'User Mention Responses', 'description': 'This chart shows the responses to user mentions over time.'}, 
    'user_content_sharing_patterns': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35], 'title': 'User Content Sharing Patterns', 'description': 'This chart shows the patterns of content sharing by users over time.'}
}

@app.route('/')
def index():
    return render_template('dashboard.html', analytics_list=analytics_data)

@app.route('/analytics', methods=['POST'])
def show_analytic():
    selected_analytic = request.form.get('analytic')
    data = analytics_data.get(selected_analytic, {})
    return render_template('analytic.html', analytic=selected_analytic, data=data)

if __name__ == '__main__':
    app.run(debug=True)
