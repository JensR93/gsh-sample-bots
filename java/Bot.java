/** gsh-sample-bots/java — minimaler Dauerlaeufer fuer den Egg-Smoke (Java Generic, Egg 121). */
public final class Bot {
    public static void main(String[] args) throws InterruptedException {
        long start = System.currentTimeMillis();
        String version = System.getProperty("java.version");
        System.out.println("[gsh-sample-bot] java " + version + " gestartet");
        while (true) {
            long seconds = (System.currentTimeMillis() - start) / 1000L;
            System.out.println("[gsh-sample-bot] java " + version + " läuft seit " + seconds + "s");
            Thread.sleep(30_000L);
        }
    }
}
