from flask import Flask, render_template, request
from code_file import get_user_hashtag_usage_trend

app = Flask(__name__)

# Dummy data for the analytics (in a real application, this would come from a database or API)
analytics_data = {
    'user_hashtag_usage_trend': {'chart_type': 'line', 'data':  get_user_hashtag_usage_trend()},
    'bot_activity_tracker': {'chart_type': 'line', 'data': [10, 15, 20, 25, 30, 35, 40]},
    'content_moderation_alerts': {'chart_type': 'bar', 'data': [5, 10, 15, 5, 20, 25, 30]},
    'poll_participation_rate': {'chart_type': 'line', 'data': [70, 65, 75, 80, 85, 90, 95]},
    'message_deletion_statistics': {'chart_type': 'bar', 'data': [20, 15, 25, 30, 10, 5, 0]},
    'event_attendance': {'chart_type': 'line', 'data': [50, 75, 100, 125, 150, 175, 200]},
    'call_participation': {'chart_type': 'bar', 'data': [30, 40, 50, 60, 70, 80, 90]},
    'group_mention_tracker': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35]},
    'scheduled_message_success_rate': {'chart_type': 'line', 'data': [90, 92, 89, 94, 87, 95, 96]},
    'spam_detection_count': {'chart_type': 'line', 'data': [5, 3, 6, 2, 7, 4, 1]},
    'read_receipts_analysis': {'chart_type': 'line', 'data': [150, 160, 170, 180, 190, 200, 210]},
    'message_edit_history': {'chart_type': 'bar', 'data': [10, 12, 8, 15, 7, 13, 9]},
    'user_reported_issues': {'chart_type': 'line', 'data': [2, 5, 3, 4, 1, 6, 2]},
    'moderation_response_time': {'chart_type': 'bar', 'data': [5, 10, 15, 20, 25, 30, 35]},
    'keyword_alerts': {'chart_type': 'line', 'data': [10, 9, 11, 14, 8, 12, 10]},
    'group_profile_updates': {'chart_type': 'line', 'data': [1, 2, 1, 3, 0, 1, 2]},
    'automated_moderation_actions': {'chart_type': 'bar', 'data': [5, 10, 15, 10, 5, 0, 5]},
    'external_link_clicks': {'chart_type': 'line', 'data': [50, 60, 70, 80, 90, 100, 110]},
    'user_invites_tracker': {'chart_type': 'bar', 'data': [10, 15, 20, 25, 30, 35, 40]},
    'group_announcement_reach': {'chart_type': 'bar', 'data': [100, 150, 200, 250, 300, 350, 400]},
    'user_mention_count': {'chart_type': 'line', 'data': [20, 25, 30, 35, 40, 45, 50]},
    'user_complaints_and_feedback': {'chart_type': 'bar', 'data': [5, 10, 15, 10, 5, 0, 5]},
    'group_expense_tracking': {'chart_type': 'line', 'data': [100, 200, 300, 250, 350, 400, 450]},
    'user_profile_picture_changes': {'chart_type': 'line', 'data': [5, 10, 5, 15, 10, 20, 15]},
    'message_flagging_for_review': {'chart_type': 'bar', 'data': [3, 6, 2, 5, 4, 7, 1]},
    'user_onboarding_completion': {'chart_type': 'bar', 'data': [90, 85, 95, 80, 75, 70, 100]},
    'user_engagement_by_hour': {'chart_type': 'bar', 'data': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]},
    'group_announcement_effectiveness': {'chart_type': 'line', 'data': [80, 85, 90, 95, 100, 105, 110]},
    'user_feedback_trend': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35]},
    'group_discussion_complexity': {'chart_type': 'line', 'data': [1.5, 1.7, 1.6, 1.8, 1.9, 2.0, 2.1]},
    'group_mention_impact': {'chart_type': 'line', 'data': [10, 15, 20, 25, 30, 35, 40]},
    'user_satisfaction_ratings': {'chart_type': 'bar', 'data': [4.5, 4.7, 4.6, 4.8, 4.9, 5.0, 4.8]},
    'user_activity_patterns': {'chart_type': 'line', 'data': [10, 20, 30, 40, 50, 60, 70]},
    'group_content_moderation': {'chart_type': 'bar', 'data': [5, 10, 15, 20, 25, 30, 35]},
    'user_invitation_conversion': {'chart_type': 'line', 'data': [50, 55, 60, 65, 70, 75, 80]},
    'user_message_edit_rate': {'chart_type': 'line', 'data': [5, 10, 15, 10, 5, 0, 5]},
    'group_event_participation': {'chart_type': 'bar', 'data': [20, 40, 60, 80, 100, 120, 140]},
    'group_notification_responses': {'chart_type': 'line', 'data': [10, 20, 30, 40, 50, 60, 70]},
    'group_keyword_tracking': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35]},
    'group_fundraising_efforts': {'chart_type': 'line', 'data': [1000, 2000, 3000, 4000, 5000, 6000, 7000]},
    'user_mention_responses': {'chart_type': 'bar', 'data': [10, 20, 30, 40, 50, 60, 70]},
    'user_content_sharing_patterns': {'chart_type': 'line', 'data': [5, 10, 15, 20, 25, 30, 35]},
}

@app.route('/')
def index():
    return render_template('dashboard.html', analytics_list=analytics_data.keys())

@app.route('/analytics', methods=['POST'])
def show_analytic():
    selected_analytic = request.form.get('analytic')
    data = analytics_data.get(selected_analytic, {})
    return render_template('analytic.html', analytic=selected_analytic, data=data)

if __name__ == '__main__':
    app.run(debug=True)
