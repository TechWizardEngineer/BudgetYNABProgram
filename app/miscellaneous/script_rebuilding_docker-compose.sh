#Step 1: Checking Dockerfile
echo "Step 1: Checking Dockerfile"
echo ""
echo "Step 2.1: Checking docker-compose.yml and assign ports"
echo ""
echo "Step 2.2: Run script_clean_docker_space to rebuild it"
echo ""
echo "Step3: Run docker-compose build, if there are major changes in app"
docker-compose build
echo ""
echo "Step4: Check result with docker-compose up"
docker-compose up
echo ""
echo "Step5: If this docker that has been rebuild works, it is the one that can use with the Docker App "

