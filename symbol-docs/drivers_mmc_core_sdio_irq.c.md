# drivers/mmc/core/sdio_irq.c

Subsystem: drivers/mmc

## Functions (11)

### process_sdio_pending_irqs
- Return type: static int
- Signature: process_sdio_pending_irqs(struct mmc_host * host)
- Line: 58

### sdio_card_irq_get
- Return type: static int
- Signature: sdio_card_irq_get(struct mmc_card * card)
- Line: 224

### sdio_card_irq_put
- Return type: static int
- Signature: sdio_card_irq_put(struct mmc_card * card)
- Line: 249

### sdio_claim_irq
- Return type: int
- Signature: sdio_claim_irq(struct sdio_func * func,sdio_irq_handler_t * handler)
- Line: 299

### sdio_get_pending_irqs
- Return type: static int
- Signature: sdio_get_pending_irqs(struct mmc_host * host,u8 * pending)
- Line: 30

### sdio_irq_thread
- Return type: static int
- Signature: sdio_irq_thread(void * _host)
- Line: 139

### sdio_irq_work
- Return type: void
- Signature: sdio_irq_work(struct work_struct * work)
- Line: 124

### sdio_release_irq
- Return type: int
- Signature: sdio_release_irq(struct sdio_func * func)
- Line: 342

### sdio_run_irqs
- Return type: static void
- Signature: sdio_run_irqs(struct mmc_host * host)
- Line: 113

### sdio_signal_irq
- Return type: void
- Signature: sdio_signal_irq(struct mmc_host * host)
- Line: 132

### sdio_single_irq_set
- Return type: static void
- Signature: sdio_single_irq_set(struct mmc_card * card)
- Line: 271
