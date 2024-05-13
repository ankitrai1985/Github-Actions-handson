# Start with a base image containing Java runtime (Java 17)
FROM openjdk:17-jdk-alpine

# Add Maintainer Info
LABEL maintainer="ankitrai1985@github.com"

# Set application's JAR file
ARG JAR_FILE=target/*.jar

# Add the application's JAR file to the container
ADD ${JAR_FILE} app.jar

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the JAR file 
ENTRYPOINT ["java","-jar","/app.jar"]
