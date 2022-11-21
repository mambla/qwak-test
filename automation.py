from qwak.automations import Automation, \
    ScheduledTrigger, MetricBasedTrigger, SqlMetric, \
    QwakBuildDeploy, BuildSpecifications, BuildMetric, ThresholdDirection, DeploymentSpecifications, SlackNotification


test_automation = Automation(
    name="bla_automation",
    model_id="bla_model",
    trigger=ScheduledTrigger(cron="*/3 * * * *"),
    action=QwakBuildDeploy(
        build_spec=BuildSpecifications(git_uri="https://github.com/mambla/qwak-test",
                                       git_branch="master",
                                       main_dir="main",
                                       tags=["test"]),
        deployment_condition=BuildMetric(metric_name="f1_score",
                                         direction=ThresholdDirection.ABOVE,
                                         threshold="100"),
        deployment_spec=DeploymentSpecifications(number_of_pods=1,
                                                 cpu_fraction=2.0,
                                                 memory="2Gi",
                                                 variation_name="B")
    ),
    on_error=SlackNotification("https://ea1f-77-137-37-186.eu.ngrok.io/error/&q=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"),
    on_success=SlackNotification("https://ea1f-77-137-37-186.eu.ngrok.io/success&q=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX")
)