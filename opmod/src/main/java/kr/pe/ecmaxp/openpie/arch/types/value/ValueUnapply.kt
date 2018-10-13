package kr.pe.ecmaxp.openpie.arch.types.value

import li.cil.oc.api.machine.Machine
import li.cil.oc.api.machine.Value

class ValueUnapply(value: Value, vararg args: Any?) : ValueInvokeable(value, *args) {
    override operator fun invoke(machine: Machine): ValueResult {
        return try {
            ValueResult(value.unapply(machine, this.args))
        } catch (e: Error) {
            ValueResult(error = e)
        } catch (e: Exception) {
            ValueResult(error = e)
        }
    }

    companion object {
        fun fromArray(array: Array<*>): ValueUnapply? {
            if (array.size < 1)
                return null

            val args = arrayOfNulls<Any?>(array.size - 1)
            System.arraycopy(array, 1, args, 0, args.size - 1)

            return ValueUnapply(array[0] as Value, *args)
        }
    }
}
