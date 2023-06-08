FROM ros:noetic-ros-core

RUN apt-get update && \
    apt-get install -y --no-install-recommends g++ \
    make \
    git \
    python3-serial \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Clone develop branch of temper-ros into docker container temper-ros
RUN git clone -b develop https://github.com/camilleconcepcion3012/temper-ros.git /home/halo_ws/src/temper-ros

WORKDIR /home/halo_ws
RUN /ros_entrypoint.sh catkin_make && sed -i '$isource "/home/halo_ws/devel/setup.bash"' /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
