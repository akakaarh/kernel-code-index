# drivers/spi/spidev.c

Subsystem: drivers/spi

## Functions (18)

### spidev_acpi_check
- Return type: static int
- Signature: spidev_acpi_check(struct device * dev)
- Line: 743

### spidev_compat_ioc_message
- Return type: static long
- Signature: spidev_compat_ioc_message(struct file * filp,unsigned int cmd,unsigned long arg)
- Line: 507

### spidev_compat_ioctl
- Return type: static long
- Signature: spidev_compat_ioctl(struct file * filp,unsigned int cmd,unsigned long arg)
- Line: 556

### spidev_exit
- Return type: static void __exit
- Signature: spidev_exit(void)
- Line: 888

### spidev_get_ioc_message
- Return type: static spi_ioc_transfer *
- Signature: spidev_get_ioc_message(unsigned int cmd,struct spi_ioc_transfer __user * u_ioc,unsigned * n_ioc)
- Line: 327

### spidev_init
- Return type: static int __init
- Signature: spidev_init(void)
- Line: 861

### spidev_ioctl
- Return type: static long
- Signature: spidev_ioctl(struct file * filp,unsigned int cmd,unsigned long arg)
- Line: 350

### spidev_message
- Return type: static int
- Signature: spidev_message(struct spidev_data * spidev,struct spi_ioc_transfer * u_xfers,unsigned n_xfers)
- Line: 205

### spidev_of_check
- Return type: static int
- Signature: spidev_of_check(struct device * dev)
- Line: 712

### spidev_open
- Return type: static int
- Signature: spidev_open(struct inode * inode,struct file * filp)
- Line: 569

### spidev_probe
- Return type: static int
- Signature: spidev_probe(struct spi_device * spi)
- Line: 765

### spidev_read
- Return type: static ssize_t
- Signature: spidev_read(struct file * filp,char __user * buf,size_t count,loff_t * f_pos)
- Line: 140

### spidev_release
- Return type: static int
- Signature: spidev_release(struct inode * inode,struct file * filp)
- Line: 620

### spidev_remove
- Return type: static void
- Signature: spidev_remove(struct spi_device * spi)
- Line: 823

### spidev_sync_read
- Return type: static ssize_t
- Signature: spidev_sync_read(struct spidev_data * spidev,size_t len)
- Line: 121

### spidev_sync_unlocked
- Return type: static ssize_t
- Signature: spidev_sync_unlocked(struct spi_device * spi,struct spi_message * message)
- Line: 93

### spidev_sync_write
- Return type: static ssize_t
- Signature: spidev_sync_write(struct spidev_data * spidev,size_t len)
- Line: 105

### spidev_write
- Return type: static ssize_t
- Signature: spidev_write(struct file * filp,const char __user * buf,size_t count,loff_t * f_pos)
- Line: 175

## Structs (1)

### spidev_data
- Line: 70
- Members:
  - devt: dev_t
  - spi_lock: mutex
  - spi: spi_device *
  - device_entry: list_head
  - users: unsigned
  - tx_buffer: u8 *
  - rx_buffer: u8 *
  - speed_hz: u32

## Variables (7)

- static **bufsiz** : unsigned (line 86)
- static **spidev_acpi_ids** : const struct acpi_device_id[] (line 749)
- static **spidev_class** : const struct class (line 679)
- static **spidev_dt_ids** : const struct of_device_id[] (line 721)
- static **spidev_fops** : const struct file_operations (line 658)
- static **spidev_spi_driver** : spi_driver (line 842)
- static **spidev_spi_ids** : const struct spi_device_id[] (line 687)

## Macros (4)

- **N_SPI_MINORS** (line 44)
- **SPIDEV_MAJOR** (line 43)
- **SPI_MODE_MASK** (line 62)
- **spidev_compat_ioctl** (line 566)
