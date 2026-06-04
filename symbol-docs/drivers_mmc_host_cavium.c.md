# drivers/mmc/host/cavium.c

Subsystem: drivers/mmc

## Functions (34)

### check_status
- Return type: static int
- Signature: check_status(u64 rsp_sts)
- Line: 409

### check_switch_errors
- Return type: static void
- Signature: check_switch_errors(struct cvm_mmc_host * host)
- Line: 165

### cleanup_dma
- Return type: static void
- Signature: cleanup_dma(struct cvm_mmc_host * host,u64 rsp_sts)
- Line: 424

### clear_bus_id
- Return type: static void
- Signature: clear_bus_id(u64 * reg)
- Line: 178

### cvm_mmc_dma_request
- Return type: static void
- Signature: cvm_mmc_dma_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 649

### cvm_mmc_get_cr_mods
- Return type: static cvm_mmc_cr_mods
- Signature: cvm_mmc_get_cr_mods(struct mmc_command * cmd)
- Line: 121

### cvm_mmc_init_lowlevel
- Return type: static int
- Signature: cvm_mmc_init_lowlevel(struct cvm_mmc_slot * slot)
- Line: 911

### cvm_mmc_interrupt
- Return type: irqreturn_t
- Signature: cvm_mmc_interrupt(int irq,void * dev_id)
- Line: 435

### cvm_mmc_of_parse
- Return type: static int
- Signature: cvm_mmc_of_parse(struct device * dev,struct cvm_mmc_slot * slot)
- Line: 947

### cvm_mmc_of_slot_probe
- Return type: int
- Signature: cvm_mmc_of_slot_probe(struct device * dev,struct cvm_mmc_host * host)
- Line: 1007

### cvm_mmc_of_slot_remove
- Return type: int
- Signature: cvm_mmc_of_slot_remove(struct cvm_mmc_slot * slot)
- Line: 1071

### cvm_mmc_request
- Return type: static void
- Signature: cvm_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 750

### cvm_mmc_reset_bus
- Return type: static void
- Signature: cvm_mmc_reset_bus(struct cvm_mmc_slot * slot)
- Line: 250

### cvm_mmc_set_clock
- Return type: static void
- Signature: cvm_mmc_set_clock(struct cvm_mmc_slot * slot,unsigned int clock)
- Line: 904

### cvm_mmc_set_ios
- Return type: static void
- Signature: cvm_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 822

### cvm_mmc_switch_to
- Return type: static void
- Signature: cvm_mmc_switch_to(struct cvm_mmc_slot * slot)
- Line: 271

### do_read
- Return type: static void
- Signature: do_read(struct cvm_mmc_host * host,struct mmc_request * req,u64 dbuf)
- Line: 298

### do_read_request
- Return type: static void
- Signature: do_read_request(struct cvm_mmc_host * host,struct mmc_request * mrq)
- Line: 707

### do_switch
- Return type: static void
- Signature: do_switch(struct cvm_mmc_host * host,u64 emm_switch)
- Line: 200

### do_write
- Return type: static void
- Signature: do_write(struct mmc_request * req)
- Line: 334

### do_write_request
- Return type: static void
- Signature: do_write_request(struct cvm_mmc_host * host,struct mmc_request * mrq)
- Line: 713

### finish_dma
- Return type: static int
- Signature: finish_dma(struct cvm_mmc_host * host,struct mmc_data * data)
- Line: 401

### finish_dma_sg
- Return type: static int
- Signature: finish_dma_sg(struct cvm_mmc_host * host,struct mmc_data * data)
- Line: 381

### finish_dma_single
- Return type: static int
- Signature: finish_dma_single(struct cvm_mmc_host * host,struct mmc_data * data)
- Line: 373

### get_bus_id
- Return type: static int
- Signature: get_bus_id(u64 reg)
- Line: 191

### get_dma_dir
- Return type: static int
- Signature: get_dma_dir(struct mmc_data * data)
- Line: 368

### prepare_dma
- Return type: static u64
- Signature: prepare_dma(struct cvm_mmc_host * host,struct mmc_data * data)
- Line: 617

### prepare_dma_sg
- Return type: static u64
- Signature: prepare_dma_sg(struct cvm_mmc_host * host,struct mmc_data * data)
- Line: 552

### prepare_dma_single
- Return type: static u64
- Signature: prepare_dma_single(struct cvm_mmc_host * host,struct mmc_data * data)
- Line: 516

### prepare_ext_dma
- Return type: static u64
- Signature: prepare_ext_dma(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 625

### set_bus_id
- Return type: static void
- Signature: set_bus_id(u64 * reg,int bus_id)
- Line: 185

### set_cmd_response
- Return type: static void
- Signature: set_cmd_response(struct cvm_mmc_host * host,struct mmc_request * req,u64 rsp_sts)
- Line: 340

### set_wdog
- Return type: static void
- Signature: set_wdog(struct cvm_mmc_slot * slot,unsigned int ns)
- Line: 236

### switch_val_changed
- Return type: static bool
- Signature: switch_val_changed(struct cvm_mmc_slot * slot,u64 new_val)
- Line: 228

## Variables (3)

- static **cvm_mmc_cr_types** : cvm_mmc_cr_type[] (line 54)
- **cvm_mmc_irq_names** : const char * [] (line 31)
- static **cvm_mmc_ops** : const struct mmc_host_ops (line 897)
