# drivers/mmc/core/debugfs.c

Subsystem: drivers/mmc

## Functions (14)

### mmc_add_card_debugfs
- Return type: void
- Signature: mmc_add_card_debugfs(struct mmc_card * card)
- Line: 386

### mmc_add_host_debugfs
- Return type: void
- Signature: mmc_add_host_debugfs(struct mmc_host * host)
- Line: 353

### mmc_caps2_set
- Return type: static int
- Signature: mmc_caps2_set(void * data,u64 val)
- Line: 331

### mmc_caps_get
- Return type: static int
- Signature: mmc_caps_get(void * data,u64 * val)
- Line: 304

### mmc_caps_set
- Return type: static int
- Signature: mmc_caps_set(void * data,u64 val)
- Line: 310

### mmc_clock_opt_get
- Return type: static int
- Signature: mmc_clock_opt_get(void * data,u64 * val)
- Line: 202

### mmc_clock_opt_set
- Return type: static int
- Signature: mmc_clock_opt_set(void * data,u64 val)
- Line: 211

### mmc_err_state_get
- Return type: static int
- Signature: mmc_err_state_get(void * data,u64 * val)
- Line: 229

### mmc_err_stats_open
- Return type: static int
- Signature: mmc_err_stats_open(struct inode * inode,struct file * file)
- Line: 281

### mmc_err_stats_show
- Return type: static int
- Signature: mmc_err_stats_show(struct seq_file * file,void * data)
- Line: 250

### mmc_err_stats_write
- Return type: static ssize_t
- Signature: mmc_err_stats_write(struct file * filp,const char __user * ubuf,size_t cnt,loff_t * ppos)
- Line: 286

### mmc_ios_show
- Return type: static int
- Signature: mmc_ios_show(struct seq_file * s,void * data)
- Line: 37

### mmc_remove_card_debugfs
- Return type: void
- Signature: mmc_remove_card_debugfs(struct mmc_card * card)
- Line: 401

### mmc_remove_host_debugfs
- Return type: void
- Signature: mmc_remove_host_debugfs(struct mmc_host * host)
- Line: 381

## Variables (2)

- static **fail_request** : char * (line 30)
- static **mmc_err_stats_fops** : const struct file_operations (line 297)
