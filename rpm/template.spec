Name:           ros-melodic-towr-ros
Version:        1.3.1
Release:        1%{?dist}
Summary:        ROS towr_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/ethz-adrl/towr
Source0:        %{name}-%{version}.tar.gz

Requires:       ncurses-devel
Requires:       ros-melodic-message-generation
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-towr
Requires:       ros-melodic-visualization-msgs
Requires:       ros-melodic-xpp-hyq
Requires:       ros-melodic-xpp-msgs
Requires:       ros-melodic-xpp-states
Requires:       xterm
BuildRequires:  ncurses-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-message-runtime
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-towr
BuildRequires:  ros-melodic-visualization-msgs
BuildRequires:  ros-melodic-xpp-msgs
BuildRequires:  ros-melodic-xpp-states

%description
A ROS dependent wrapper for towr. Adds a keyboard user interface to set
different goal states, motions and robots and visualizes the produced motions
plan in rviz using xpp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Jul 12 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.3.1-1
- Autogenerated by Bloom

