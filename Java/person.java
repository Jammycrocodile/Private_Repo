public class Person {

    private String name;
    private int alter;
    private String nummer;
    private int kreditrahmen;

    public Modul(String modulnummer)
    {
        nummer = modulnummer;

    }

    public Person(String meinName, int meinAlter)
    {
        name = meinName;
        alter = meinAlter;
    }

    public gibAlter()
    {
        return alter;
    }

    public gibName()
    {
        return name;
    }

    public void setzeAlter(int setzeAlter)
    {
        alter = setzeAlter;
    }

    public detailsAusgeben()
    {
        System.out.println("Der Name dieser Person ist: " name );
    }
}
