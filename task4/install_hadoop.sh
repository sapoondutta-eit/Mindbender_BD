sudo apt update
sudo apt install openssh-server openssh-client -y
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
cd opt
wget http://archive.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
tar -xzf hadoop-2.7.3.tar.gz
rm hadoop-2.7.3.tar.gz

cd 
nano bash_profile.sh
echo 'export JAVA_HOME=~/opt/jdk1.8.0_221' > ./bash_profile.sh
echo 'export PATH=$PATH:$JAVA_HOME/bin' > ./bash_profile.sh
echo 'export HADOOP_HOME= ~/opt/hadoop-2.7.3' > ./bash_profile.sh
echo 'export HADOOP_INSTALL=$HADOOP_HOME' > ./bash_profile.sh
echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME' > ./bash_profile.sh
echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME' > ./bash_profile.sh
echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME' > ./bash_profile.sh
echo 'export YARN_HOME=$HADOOP_HOME' > ./bash_profile.sh
echo 'export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native' > ./bash_profile.sh
echo 'export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin' > ./bash_profile.sh


cd home/marcus/opt/hadoop-2.7.3/etc/hadoop


echo 'export JAVA_HOME=/home/deward/opt/jdk1.8.0_221' > hadoop-env.sh

echo '<configuration> <property> <name>fs.default.name</name> <value>hdfs://localhost:9000</value> </property> </configuration>' > core-site.xml
echo '<configuration>

	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>


	<property>
		<name>dfs.name.dir</name>
		<value>file:///home/deward/opt/hadoop-2.7.3/hdfs/namenode</value>
	</property>

	<property>
		<name>dfs.name.dir</name>
		<value>file:///home/deward/opt/hadoop-2.7.3/hdfs/datanode</value>
	</property>
	
</configuration> ' > hdfs-site.xml


echo '<configuration>
	<property>
		<name>yarn.nodemanager.aux-services</name>
		<value>mapreduce_shuffle</value>
	</property>

</configuration>' > yarn-site.xml

cd ../../../../
chmod 777 opt/
cd opt/
chmod 777 hadoop-2.7.3


cd hadoop-2.7.3
mkdir hdfs
cd hdfs/
mkdir datanode 
mkdir namenode

cd ../etc/hadoop/
echo '<configuration>
	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>

	<property>
		<name>dfs.name.dir</name>
		<value>file:///home/user/opt/hadoop-2.7.3/hdfs/namenode</value>
	</property>

	<property>
		<name>dfs.name.dir</name>
		<value>file:///home/user/opt/hadoop-2.7.3/hdfs/datanode</value>
	</property>
</configuration>
' > hdfs-site.xml

cp mapred-site.xml.template mapred-site.xml

echo '<configuration>
	<property>
		<name>mapreduce.framework.name</name>
		<value>yarn</value>
	</property>
</configuration>' > mapred-site.xml


echo '<configuration>

<!-- Site specific YARN configuration properties -->
	<property>
		<name>yarn.nodemanager.aux-services</name>
		<value>mapreduce_shuffle</value>
	</property>

</configuration>' > yarn-site.xml

cd 

source .bash_profile

OUTPUT=$(start-all.sh)











