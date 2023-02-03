###---------------------------------------------------
## Using instructions from
## https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes
###---------------------------------------------------

#1. Listing docker container activated
echo "Step 1: This are the activated docker containers\n"
docker ps -a
echo ""

#2. Removing activated docker containers
echo "Step 2: Stopping container to remove them\n"
docker stop $(docker ps -a -q)
echo ""

#2. Removing activated docker containers
echo "Step 3: Removing containers that were removed\n"
docker rm $(docker ps -a -q)

#4. Checking if previous step was OK
echo "Step 4: Checking if previous step was OK\n"
docker ps -a
echo ""

#5 Checking if images and volumes are up
echo "Step 5.1: Checking if volumes are up\n"
docker volume ls
echo ""

echo "Step 5.2: Checking if images and volumes are up"
docker images
echo ""

echo "Step 5.3: Removing images according to list"
docker rmi $(docker images -a -q)
echo ""


