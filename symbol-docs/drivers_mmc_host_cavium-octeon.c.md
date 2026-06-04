# drivers/mmc/host/cavium-octeon.c

Subsystem: drivers/mmc

## Functions (13)

### l2c_lock_line
- Return type: static void
- Signature: l2c_lock_line(u64 addr)
- Line: 40

### l2c_lock_mem_region
- Return type: static void
- Signature: l2c_lock_mem_region(u64 start,u64 len)
- Line: 60

### l2c_unlock_line
- Return type: static void
- Signature: l2c_unlock_line(u64 addr)
- Line: 50

### l2c_unlock_mem_region
- Return type: static void
- Signature: l2c_unlock_mem_region(u64 start,u64 len)
- Line: 76

### octeon_mmc_acquire_bus
- Return type: static void
- Signature: octeon_mmc_acquire_bus(struct cvm_mmc_host * host)
- Line: 90

### octeon_mmc_dmar_fixup
- Return type: static void
- Signature: octeon_mmc_dmar_fixup(struct cvm_mmc_host * host,struct mmc_command * cmd,struct mmc_data * data,u64 addr)
- Line: 127

### octeon_mmc_dmar_fixup_done
- Return type: static void
- Signature: octeon_mmc_dmar_fixup_done(struct cvm_mmc_host * host)
- Line: 141

### octeon_mmc_int_enable
- Return type: static void
- Signature: octeon_mmc_int_enable(struct cvm_mmc_host * host,u64 val)
- Line: 110

### octeon_mmc_probe
- Return type: static int
- Signature: octeon_mmc_probe(struct platform_device * pdev)
- Line: 149

### octeon_mmc_release_bus
- Return type: static void
- Signature: octeon_mmc_release_bus(struct cvm_mmc_host * host)
- Line: 102

### octeon_mmc_remove
- Return type: static void
- Signature: octeon_mmc_remove(struct platform_device * pdev)
- Line: 298

### octeon_mmc_set_shared_power
- Return type: static void
- Signature: octeon_mmc_set_shared_power(struct cvm_mmc_host * host,int dir)
- Line: 117

### phys_to_ptr
- Return type: static void *
- Signature: phys_to_ptr(u64 address)
- Line: 31

## Variables (2)

- static **octeon_mmc_driver** : platform_driver (line 326)
- static **octeon_mmc_match** : const struct of_device_id[] (line 315)

## Macros (1)

- **CVMX_MIO_BOOT_CTL** (line 22)
