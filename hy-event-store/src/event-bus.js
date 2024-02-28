class HYEventBus {
  constructor() {
    this.eventBus = {}
  }

  on(eventName, eventCallback, thisArg) {
    if (typeof eventName !== "string") {
      throw new TypeError("the event name must be string type")
    }

    if (typeof eventCallback !== "function") {
      throw new TypeError("the event callback must be function type")
    }

    let handlers = this.eventBus[eventName]
    if (!handlers) {
      handlers = []
      this.eventBus[eventName] = handlers
    }

    handlers.push({
      eventCallback,
      thisArg
    })
    return this
  }

  once(eventName, eventCallback, thisArg) {
    if (typeof eventName !== "string") {
      throw new TypeError("the event name must be string type")
    }

    if (typeof eventCallback !== "function") {
      throw new TypeError("the event callback must be function type")
    }

    const tempCallback = (...payload) => {
      this.off(eventName, tempCallback)
      eventCallback.apply(thisArg, payload)
    }

    return this.on(eventName, tempCallback, thisArg)
  }

  // 触发事件：执行事件对应的所有回调
  emit(eventName, ...payload) {
    if (typeof eventName !== "string") {
      throw new TypeError("the event name must be string type")
    }

    const handlers = this.eventBus[eventName] || []
    handlers.forEach(handler => {
      handler.eventCallback.apply(handler.thisArg, payload)
    })
    return this
  }

  // 注销事件：清除事件对应的所有回调
  off(eventName, eventCallback) {
    if (typeof eventName !== "string") {
      throw new TypeError("the event name must be string type")
    }

    if (typeof eventCallback !== "function") {
      throw new TypeError("the event callback must be function type")
    }

    const handlers = this.eventBus[eventName]
    if (handlers && eventCallback) {
      // 为什么还要拷贝：如果有两个相同的回调，原数组移除handler后会影响索引
      // 若对同一个函数监听多次且它在数组中的位置是相邻的， 比如[1,1,2,3]，现在我们要删除1，那么splice(0, 1)后，i变成了1，但现在0位置还剩一个1没有被删除
      const newHandlers = [...handlers]
      for (let i = 0; i < newHandlers.length; i++) {
        const handler = newHandlers[i]
        if (handler.eventCallback === eventCallback) {
          const index = handlers.indexOf(handler)
          handlers.splice(index, 1)
        }
      }
    }

    if (handlers.length === 0) {
      delete this.eventBus[eventName]
    }
  }

  clear() {
    this.emitBus = {}
  }

  hasEvent(eventName) {
    return Object.keys(this.emitBus).includes(eventName)
  }
}

module.exports = HYEventBus
