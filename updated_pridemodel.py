
def generate_report(data):
    expert_note = {
        "Attention": "Improve your focus and concentration to boost productivity and minimize errors in your work.",
        "Memory": "Develop effective memory retention techniques to facilitate learning and recall of critical information.",
        "Critical Thinking": "Cultivate your analytical reasoning skills to evaluate complex problems and make informed decisions.",
        "Creative Thinking": "Foster innovative thinking to generate unique solutions and approaches to challenges.",
        "Mindset": "Embrace a growth mindset, believing in your ability to learn and develop skills through dedication and effort.",
        "Attitude": "Cultivate a positive mindset to navigate challenges with resilience and optimism.",
        "Expression": "Hone your communication skills to articulate ideas clearly and persuasively across various platforms.",
        "Communication": "Enhance your ability to convey information effectively and build meaningful connections through communication.",
        "Collaboration": "Strengthen your collaborative skills to work effectively within teams and achieve collective goals.",
        "Leadership": "Develop your leadership capabilities to inspire and guide others toward achieving shared objectives.",
        "Awareness": "Expand your awareness of global issues and trends to make informed decisions and drive positive change.",
        "Application": "Apply your knowledge and skills effectively in practical situations to achieve tangible results.",
        "Advantage": "Leverage your unique strengths and capabilities to gain a competitive edge and create opportunities for success."
    }

    action_plan = ""
    for skill, value_points in data.items():
        if skill in expert_note:
            action_plan += f"PRIDE: {skill}\n\n"
            action_plan += f"{expert_note[skill]}\n\n"

            if value_points < 50:
                action_plan += f"{data.get('student_name', 'The student')} needs to focus on building a strong foundation in {skill.lower()}.\n\n"
            else:
                action_plan += f"{data.get('student_name', 'The student')} has demonstrated proficiency in {skill.lower()}, but there's always room for improvement.\n\n"

    template = """
    PRIDE Holistic Personality Summary for {student_name}

    1. Overview of Performance
    The report provides a holistic assessment of {student_name}'s performance across various skills and metrics. Key values and metrics include:
    - Attention
    - Memory
    - Critical Thinking
    - Creative Thinking
    - Mindset
    - Attitude
    - Expression
    - Communication
    - Collaboration
    - Leadership
    - Awareness
    - Application
    - Advantage
    
    2. Detailed Description
    Each skill is evaluated with detailed descriptions and insights:
    {generate_detailed_description(data)}

    3. Ranking Order
    The Ranking Order section arranges activities based on the Index scores of PRIDE, Skills, and Intelligence Domains. Activities with higher Index scores are ranked higher, providing insight into {data["student_name"]}'s strengths and areas for improvement. This ranking helps identify {data["student_name"]}'s key strengths and pinpoint areas where additional focus and effort may yield significant improvements.
    {generate_ranking_order(data)}

    4. Polarity Order
    The Polarity Order section highlights the positive and negative aspects of each skill contribution, ranked in descending order based on their values.
    {generate_polarity_order(data)}

    5. Areas for Improvement
    Areas for Improvement are identified based on contributions that fall below the optimal threshold. Focusing on these areas can help {data["student_name"]} enhance their overall performance and achieve greater success. Specific improvements include:
    {generate_areas_for_improvement(data)}

    6. Future Outlook
    Looking ahead, {data["student_name"]} has great potential to continue progressing in their personal and academic journey. Continued focus on their strengths and targeted improvements in identified areas will pave the way for {data["student_name"]} to achieve even greater success.

    Conclusion
    This PRIDE Holistic Personality Summary provides {data["student_name"]} with valuable insights into their current capabilities and areas for development. By leveraging these insights, {data["student_name"]} can focus on enhancing their strengths and addressing areas that require improvement, ultimately achieving their academic and personal goals.

    Action Plan and Way Forward
    {generate_action_plan(data)}
    """

    report = format_template(template, student_name=data["student_name"])
    return report

def generate_detailed_description(data):
    expert_note = {
        "Attention": "Improve your focus and concentration to boost productivity and minimize errors in your work.",
        "Memory": "Develop effective memory retention techniques to facilitate learning and recall of critical information.",
        "Critical Thinking": "Cultivate your analytical reasoning skills to evaluate complex problems and make informed decisions.",
        "Creative Thinking": "Foster innovative thinking to generate unique solutions and approaches to challenges.",
        "Mindset": "Embrace a growth mindset, believing in your ability to learn and develop skills through dedication and effort.",
        "Attitude": "Cultivate a positive mindset to navigate challenges with resilience and optimism.",
        "Expression": "Hone your communication skills to articulate ideas clearly and persuasively across various platforms.",
        "Communication": "Enhance your ability to convey information effectively and build meaningful connections through communication.",
        "Collaboration": "Strengthen your collaborative skills to work effectively within teams and achieve collective goals.",
        "Leadership": "Develop your leadership capabilities to inspire and guide others toward achieving shared objectives.",
        "Awareness": "Expand your awareness of global issues and trends to make informed decisions and drive positive change.",
        "Application": "Apply your knowledge and skills effectively in practical situations to achieve tangible results.",
        "Advantage": "Leverage your unique strengths and capabilities to gain a competitive edge and create opportunities for success."
    }

    description = ""
    for skill, value_points in data.items():
        if skill in expert_note:
            description += f"{skill}: {value_points}\n{expert_note[skill]}\n\n"
    return description

def generate_ranking_order(data):
    # Implement ranking order generation logic
    return "Ranking order details..."

def generate_polarity_order(data):
    # Implement polarity order generation logic
    return "Polarity order details..."

def generate_areas_for_improvement(data):
    improvement_areas = ""
    for skill, value_points in data.items():
        if value_points < 50:
            improvement_areas += f"{skill}: Improve {skill.lower()} by focusing on relevant techniques and practices.\n"
    return improvement_areas

def generate_action_plan(data):
    # Generate an action plan based on the data
    return "Action plan details..."

def format_template(template, **kwargs):
    return template.format(**kwargs)
