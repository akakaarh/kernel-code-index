# drivers/i2c/i2c-dev.c

Subsystem: drivers/i2c

## Functions (24)

### compat_i2cdev_ioctl
- Return type: static long
- Signature: compat_i2cdev_ioctl(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 531

### get_free_i2c_dev
- Return type: static i2c_dev *
- Signature: get_free_i2c_dev(struct i2c_adapter * adap)
- Line: 68

### i2c_dev_attach_adapter
- Return type: static int __init
- Signature: i2c_dev_attach_adapter(struct device * dev,void * dummy)
- Line: 743

### i2c_dev_detach_adapter
- Return type: static int __exit
- Signature: i2c_dev_detach_adapter(struct device * dev,void * dummy)
- Line: 749

### i2c_dev_exit
- Return type: static void __exit
- Signature: i2c_dev_exit(void)
- Line: 792

### i2c_dev_get_by_minor
- Return type: static i2c_dev *
- Signature: i2c_dev_get_by_minor(unsigned index)
- Line: 53

### i2c_dev_init
- Return type: static int __init
- Signature: i2c_dev_init(void)
- Line: 759

### i2cdev_attach_adapter
- Return type: static int
- Signature: i2cdev_attach_adapter(struct device * dev)
- Line: 664

### i2cdev_check
- Return type: static int
- Signature: i2cdev_check(struct device * dev,void * addrp)
- Line: 188

### i2cdev_check_addr
- Return type: static int
- Signature: i2cdev_check_addr(struct i2c_adapter * adapter,unsigned int addr)
- Line: 228

### i2cdev_check_mux_children
- Return type: static int
- Signature: i2cdev_check_mux_children(struct device * dev,void * addrp)
- Line: 212

### i2cdev_check_mux_parents
- Return type: static int
- Signature: i2cdev_check_mux_parents(struct i2c_adapter * adapter,int addr)
- Line: 199

### i2cdev_detach_adapter
- Return type: static int
- Signature: i2cdev_detach_adapter(struct device * dev)
- Line: 703

### i2cdev_dev_release
- Return type: static void
- Signature: i2cdev_dev_release(struct device * dev)
- Line: 656

### i2cdev_ioctl
- Return type: static long
- Signature: i2cdev_ioctl(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 400

### i2cdev_ioctl_rdwr
- Return type: static noinline int
- Signature: i2cdev_ioctl_rdwr(struct i2c_client * client,unsigned nmsgs,struct i2c_msg * msgs)
- Line: 243

### i2cdev_ioctl_smbus
- Return type: static noinline int
- Signature: i2cdev_ioctl_smbus(struct i2c_client * client,u8 read_write,u8 command,u32 size,union i2c_smbus_data __user * data)
- Line: 319

### i2cdev_notifier_call
- Return type: static int
- Signature: i2cdev_notifier_call(struct notifier_block * nb,unsigned long action,void * data)
- Line: 722

### i2cdev_open
- Return type: static int
- Signature: i2cdev_open(struct inode * inode,struct file * file)
- Line: 598

### i2cdev_read
- Return type: static ssize_t
- Signature: i2cdev_read(struct file * file,char __user * buf,size_t count,loff_t * offset)
- Line: 134

### i2cdev_release
- Return type: static int
- Signature: i2cdev_release(struct inode * inode,struct file * file)
- Line: 628

### i2cdev_write
- Return type: static ssize_t
- Signature: i2cdev_write(struct file * file,const char __user * buf,size_t count,loff_t * offset)
- Line: 163

### name_show
- Return type: static ssize_t
- Signature: name_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 98

### put_i2c_dev
- Return type: static void
- Signature: put_i2c_dev(struct i2c_dev * i2c_dev,bool del_cdev)
- Line: 88

## Structs (4)

### i2c_dev
- Line: 42
- Members:
  - list: list_head
  - adap: i2c_adapter *
  - dev: device
  - cdev: cdev
  - read_write: u8
  - command: u8
  - size: u32
  - data: compat_caddr_t
  - addr: u16
  - flags: u16
  - len: u16
  - buf: compat_caddr_t
  - msgs: compat_caddr_t
  - nmsgs: u32

### i2c_msg32
- Line: 519
- Members:
  - list: list_head
  - adap: i2c_adapter *
  - dev: device
  - cdev: cdev
  - read_write: u8
  - command: u8
  - size: u32
  - data: compat_caddr_t
  - addr: u16
  - flags: u16
  - len: u16
  - buf: compat_caddr_t
  - msgs: compat_caddr_t
  - nmsgs: u32

### i2c_rdwr_ioctl_data32
- Line: 526
- Members:
  - list: list_head
  - adap: i2c_adapter *
  - dev: device
  - cdev: cdev
  - read_write: u8
  - command: u8
  - size: u32
  - data: compat_caddr_t
  - addr: u16
  - flags: u16
  - len: u16
  - buf: compat_caddr_t
  - msgs: compat_caddr_t
  - nmsgs: u32

### i2c_smbus_ioctl_data32
- Line: 512
- Members:
  - list: list_head
  - adap: i2c_adapter *
  - dev: device
  - cdev: cdev
  - read_write: u8
  - command: u8
  - size: u32
  - data: compat_caddr_t
  - addr: u16
  - flags: u16
  - len: u16
  - buf: compat_caddr_t
  - msgs: compat_caddr_t
  - nmsgs: u32

## Variables (4)

- static **i2c_attrs** : attribute * [] (line 109)
- static **i2c_dev_class** : const struct class (line 651)
- static **i2cdev_fops** : const struct file_operations (line 639)
- static **i2cdev_notifier** : notifier_block (line 737)

## Macros (3)

- **I2C_MINORS** (line 49)
- **compat_i2cdev_ioctl** (line 595)
- **pr_fmt**(fmt) (line 17)
