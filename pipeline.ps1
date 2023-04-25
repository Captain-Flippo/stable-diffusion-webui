param($runtype)

$stackname = "StableDiffusionWebUIStack"

if ($runtype -eq "run") {
    Write-Host "Running..."
    aws cloudformation create-stack --stack-name $stackname --template-body file://aws/pipeline_template.yaml
} elseif ($runtype -eq "stop") {
    Write-Host "Stopping..."
    aws cloudformation delete-stack --stack-name $stackname
} elseif ($runtype -eq "show"){
    Write-Host "Showing Pipeline ID..."
    aws cloudformation list-stack-resources --stack-name $stackname --query 'StackResourceSummaries[?ResourceType==`AWS::EC2::EIP`].PhysicalResourceId' --output text
} elseif ($runtype -eq "url") {
    Write-Host "Showing URL..."
    aws cloudformation list-stack-resources --stack-name $stackname --query 'StackResourceSummaries[?ResourceType==`AWS::EC2::EIP`].PhysicalResourceId' --output text | % { "http://$($_):7860" }
} else {
    Write-Host "Please provide a runtype parameter. Can be either 'run' or 'stop'"
}