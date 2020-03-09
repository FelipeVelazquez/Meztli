<h1> Meztli</h1> 
<h2 > Comandos para secuencia de ejecución </h2>
<h3> Instalación de recursos previos </h3>
<ul>
  <li>sudo apt-get install ros-melodic-octomap</li>
  <li>git clone https://github.com/FelipeVelazquez/RoboCar.git</li>
</ul>
<br> Añadir el espacio de trabajo de RoboCar al archivo .bashrc </br>
<h3>Hardware utilizado</h3>
<ul>
	<li>Kinect Xbox 360 V1.0 </li>
	<img src="images/Kinect.jpg" width="400"> 
	<li>Control Xbox 360 </li>
	<img src="images/control.jpg" width="400">
</ul>>
<h3> Comandos para ejecución </h3>
<ol>
  <li>roslaunch openni_launch openni.launch</li>
  <li>roslaunch pointcloud_to_laserscan start.launch</li>
  <li >rosrun odometria Odometria_Xbox.py</li>
  <li >rosrun gmapping slam_gmapping scan:=camera/scan</li>
  <li >roslaunch octomap_server octomap_mapping.launch</li>
</ol>
