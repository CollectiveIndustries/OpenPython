package kr.pe.ecmaxp.openpython.console

import kr.pe.ecmaxp.openpython.arch.OpenPythonFirmware
import kr.pe.ecmaxp.openpython.arch.OpenPythonMemoryRegion.*
import kr.pe.ecmaxp.openpython.arch.consts.KB
import kr.pe.ecmaxp.openpython.arch.consts.SYS_DEBUG
import kr.pe.ecmaxp.openpython.arch.consts.SYS_INFO_RAM_SIZE
import kr.pe.ecmaxp.thumbsf.CPU
import kr.pe.ecmaxp.thumbsf.MemoryFlag
import kr.pe.ecmaxp.thumbsf.consts.PC
import kr.pe.ecmaxp.thumbsf.signal.ControlStopSignal
import java.nio.charset.Charset
import java.time.Instant


object OpenPythonBenchmark {
    @JvmStatic
    fun main(args: Array<String>) {
        val cpu = CPU()
        val firmware = OpenPythonFirmware.v1_0_1
        cpu.memory.apply {
            flash(FLASH.address, FLASH.size, firmware.loadFirmware())
            map(SRAM.address, SRAM.size, MemoryFlag.RW) // ram
            map(RAM.address, 256 * KB, MemoryFlag.RW) // ram
            map(SYSCALL.address, SYSCALL.size, MemoryFlag.RW) // syscall
        }

        for (i in 1..10) {
            val start = Instant.now()
            cpu.regs[PC] = cpu.memory.readInt(0x08000000 + 4)

            try {
                while (true)
                    cpu.run(1000000) {
                        when (cpu.regs[7]) {
                            SYS_INFO_RAM_SIZE -> cpu.regs[0] = 64 * KB
                            0xDEADBEEFL.toInt() -> throw ControlStopSignal()
                            SYS_DEBUG -> print(String(cpu.memory.readBuffer(cpu.regs[0], cpu.regs[1]), Charset.defaultCharset()))
                            else -> cpu.regs[0] = 0;
                        }
                    }
            } catch (e: ControlStopSignal) {
                val end = Instant.now()
                println(end.toEpochMilli() - start.toEpochMilli())
            }
        }
    }
}
