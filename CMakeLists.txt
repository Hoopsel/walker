cmake_minimum_required(VERSION 2.8.3)
project(walker)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  kobuki_msgs
  roscpp
  rospy
  std_msgs
  pcl_ros
)
find_package(Boost REQUIRED)
find_package(PCL)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES 
  CATKIN_DEPENDS roscpp std_msgs pcl_ros kobuki_msgs
  DEPENDS PCL Boost
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(look_node src/look_node.cpp
						 src/look.cpp)

add_executable(runaway_node src/runaway_node.cpp
							src/runaway.cpp)

target_link_libraries(
   look_node
   ${catkin_LIBRARIES}
   ${PCL_LIBRARIES}
)
target_link_libraries(
   runaway_node
   ${catkin_LIBRARIES}
   ${PCL_LIBRARIES}
)
