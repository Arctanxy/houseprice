from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

#导入数据
mnist = input_data.read_data_sets("./MNIST_data",one_hot=True)

#设置参数
learning_rate = 0.5#学习率
epochs = 10#训练次数
batch_size = 100#每次取的样本数量

#使用占位符声明x和y
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#声明权重和偏置项

W1 = tf.Variable(tf.random_normal([784,300],stddev = 0.03),name="W1")
b1 = tf.Variable(tf.random_normal([300]),name='b1')
W2 = tf.Variable(tf.random_normal([300,10],stddev=0.03),name="W2")
b2 = tf.Variable(tf.random_normal([10]),name="b2")

#计算隐藏层
hidden_out = tf.add(tf.matmul(x,W1),b1)
hidden_out = tf.nn.relu(hidden_out)

#计算输出值
y_ = tf.nn.softmax(tf.add(tf.matmul(hidden_out,W2),b2))

#计算交叉熵
y_clipped = tf.clip_by_value(y_,1e-10,0.9999999)
cross_entropy = -tf.reduce_mean(tf.reduce_sum(y*tf.log(y_clipped) + (1 - y)*tf.log(1-y_clipped),axis=1))

#定义优化器
optimiser = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cross_entropy)

#设置初始化函数
init_op = tf.global_variables_initializer()

#设置准确率函数
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

#开始训练
with tf.Session() as sess:
    sess.run(init_op)
    total_batch = int(len(mnist.train.labels)/batch_size)
    for epoch in range(epochs):#epochs=10,训练10次
        avg_cost = 0
        for i in range(total_batch):
            batch_x ,batch_y = mnist.train.next_batch(batch_size=batch_size)
            _,c = sess.run([optimiser,cross_entropy],feed_dict={x:batch_x,
                                                                y:batch_y})
            avg_cost += c/total_batch
        print("Epoch:",(epoch+1),"cost=","{:.3f}".format(avg_cost))
    print(sess.run(accuracy,feed_dict={x:mnist.test.images,
                                       y:mnist.test.labels}))

